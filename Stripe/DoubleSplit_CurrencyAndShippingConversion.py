# Partners send us a compact string that mixes currencies, shipping methods, and a number that looks like a rate. It reads clean in the happy path, but the real world creeps in. Extra spaces, missing chunks, and odd separators show up from time to time. Our job is to turn that into something we can trust, then answer simple questions quickly. Think of a merchant asking for a conversion between two currencies and expecting a number back that reflects the rate they agreed to for a given shipping method or across methods depending on policy. The details in the string are the only source of truth during this exercise.

# Sometimes there is an obvious direct entry from one currency to another. Other times there is no direct line, yet you can still get there with an intermediate hop. We prefer a simple path that we can explain and audit. If there are several options, choose the one that best fits the question as stated. Keep your code readable, talk through your checks, and write a few targeted tests as you go.

# Let us stage the work in steps. Please think aloud and ask clarifying questions before you code.

# Step 1
# Take the raw input like

# "USD:CAD:DHL:5,USD:GBP:FEDX:10, EUR:USD:Jet1:2 "


# and parse it into a structured form. Trim spaces, ignore entries that are missing any field. Each entry has four parts, source currency, target currency, shipping method, and rate as a number. Preserve the order you find.

# Step 2
# Given the parsed data, write a function that converts an amount from a source to a target when a direct entry exists. Use the rate from the matching entry. Matching is case sensitive. If there are several matching entries with different shipping methods, pick a clear policy and state it, for example first match in the data or best rate, but keep it consistent.

# Step 3
# If there is no direct entry, return a route that gets you from source to target using intermediate currencies available in the data. Return the path of currencies, the sequence of shipping methods used, and the total cost for converting the given amount under a simple additive rule based on the rates you have. Keep the route easy to read.

# Step 4
# Produce a small summary helper that, given an amount and two currencies, returns either the direct conversion or the routed result in a single object. Include the route only when an indirect path was used. If no path exists, return a clear error object rather than raising.

# currencies, shipping methods, rate

from collections import defaultdict
import heapq

class ForeignExchange:
    def __init__(self, raw_data:str):
        self.exchange_routes = self._parse(raw_data)

    def _parse(self, raw_data: str):
        raw_routes = raw_data.split(",")
        structured_routes = []
        for raw_route in raw_routes:
            parts = [r.replace(" ", "") for r in raw_route.strip().split(":")]
            if len(parts) != 4:
                continue  # skip malformed
            source_currency, target_currency, shipping_method, rate_str = parts
            try:
                rate = float(rate_str)
            except ValueError:
                continue  # skip if rate not numeric
            structured_routes.append({
                "source": source_currency,
                "target": target_currency,
                "method": shipping_method,
                "rate": float(rate_str)   # cast to float
            })

        return structured_routes
    
    def select_best_rate(self, candidates: list[dict]) -> dict | None:
        # Pick the entry with the lowest numeric rate; return None if empty.
        if not candidates:
            return None
        best_entry = candidates[0]
        for entry in candidates[1:]:
            if entry["rate"] < best_entry["rate"]:
                best_entry = entry
        return best_entry
    
    def convert_direct(self, raw_data: str, source_currency: str, target_currency: str, amount: float) -> dict:
        # Parse routes, find all direct quotes from source_currency to target_currency,
        # compute amount_out for each, then return the best by lowest rate.
        routes = self._parse(raw_data)  # expects dicts with keys: source, target, method, rate
        direct_quotes: list[dict] = []

        for route in routes:
            if route["source"] == source_currency and route["target"] == target_currency:
                rate = route["rate"]
                method = route["method"]
                direct_quotes.append({
                    "source": source_currency,
                    "target": target_currency,
                    "method": method,
                    "rate": rate,
                    "amount_in": float(amount),
                    "amount_out": float(amount * rate),
                })

        if not direct_quotes:
            return {"error": f"No direct rate from {source_currency} to {target_currency}"}

        return self.select_best_rate(direct_quotes)
    

    # ===== Step 3: routed conversion when no direct entry exists =====
    def convert_routed(self, raw_data: str, source: str, target: str, amount: float) -> dict:
        """
        Find an indirect path. Policy: minimize total summed rate, then fewer hops, then earlier input order.
        Cost model: total_rate is the sum of leg rates, amount_out equals amount * total_rate.
        """
        routes = self._parse(raw_data)
        adj = defaultdict(list)
        for i, r in enumerate(routes):
            adj[r["source"]].append((r["target"], r["method"], r["rate"], i))

        INF = (float("inf"), float("inf"), float("inf"))
        best = defaultdict(lambda: INF)
        best[source] = (0.0, 0, -1)
        prev: dict[str, tuple[str, str, float]] = {}
        heap = [(0.0, 0, -1, source)]

        while heap:
            rate, hops, ord_idx, u = heapq.heappop(heap)
            if (rate, hops, ord_idx) != best[u]:
                continue
            if u == target:
                break
            for v, method, r, oi in adj.get(u, []):
                cand = (rate + r, hops + 1, oi)
                if cand < best[v]:
                    best[v] = cand
                    prev[v] = (u, method, r)
                    heapq.heappush(heap, (*cand, v))

        if best[target] == INF:
            return {"error": f"No path from {source} to {target}"}

        # reconstruct
        path_currencies, path_methods, legs = [target], [], []
        node = target
        while node != source:
            u, m, r = prev[node]
            path_currencies.append(u)
            path_methods.append(m)
            legs.append({"from": u, "to": node, "method": m, "rate": r})
            node = u
        path_currencies.reverse()
        path_methods.reverse()
        legs.reverse()

        total_rate = best[target][0]
        amount_in = float(amount)
        return {
            "source": source,
            "target": target,
            "amount_in": amount_in,
            "total_rate": float(total_rate),
            "amount_out": float(amount_in * total_rate),
            "route": {
                "currencies": path_currencies,
                "methods": path_methods,
                "legs": legs
            }
        }

    # ===== Step 4: summary helper =====
    def convert_best(self, raw_data: str, source_currency: str, target_currency: str, amount: float) -> dict:
        """
        Try direct first. If not found, return routed result.
        Include route only for indirect paths. Return an error object when no path exists.
        """
        direct = self.convert_direct(raw_data, source_currency, target_currency, amount)
        if "error" not in direct:
            return direct
        routed = self.convert_routed(raw_data, source_currency, target_currency, amount)
        return routed
    

# =========================
# Print style tests
# =========================

# ---------- Step 1: parsing ----------
fx = ForeignExchange("USD:CAD:DHL:5, USD:GBP:FEDX:10, EUR:USD:Jet1:2, GBP:JPY:DHL:7")
expected_1 = [
    {"source":"USD","target":"CAD","method":"DHL","rate":5.0},
    {"source":"USD","target":"GBP","method":"FEDX","rate":10.0},
    {"source":"EUR","target":"USD","method":"Jet1","rate":2.0},
    {"source":"GBP","target":"JPY","method":"DHL","rate":7.0},
]
print("parse basic happy path:", fx.exchange_routes == expected_1)

# whitespace inside fields should be removed
fx2 = ForeignExchange("USD:CAD:DHL:5, USD :GBP:FEDX:10, EU R:USD:Jet1:2, G BP:JPY:D HL:7")
expected_2 = [
    {"source":"USD","target":"CAD","method":"DHL","rate":5.0},
    {"source":"USD","target":"GBP","method":"FEDX","rate":10.0},
    {"source":"EUR","target":"USD","method":"Jet1","rate":2.0},
    {"source":"GBP","target":"JPY","method":"DHL","rate":7.0},
]
print("parse removes internal whitespace in fields:", fx2.exchange_routes == expected_2)

# malformed and non numeric rates are skipped
fx3 = ForeignExchange("USD:CAD:DHL:x, USD:CAD:Jet1:4, badrow, EUR:USD:Jet1:2.5")
expected_3 = [
    {"source":"USD","target":"CAD","method":"Jet1","rate":4.0},
    {"source":"EUR","target":"USD","method":"Jet1","rate":2.5},
]
print("parse skips malformed and non numeric:", fx3.exchange_routes == expected_3)

# ---------- Step 2: convert_direct ----------
# Ensure convert_direct uses routes = self._parse(raw_data)

# single direct route
out = fx.convert_direct("USD:CAD:DHL:5, EUR:USD:Jet1:2", "USD", "CAD", 10)
expected_out_1 = {"source":"USD","target":"CAD","method":"DHL","rate":5.0,"amount_in":10.0,"amount_out":50.0}
print("direct single route:", out == expected_out_1, out)

# multiple direct routes, pick lowest rate
out = fx.convert_direct("USD:CAD:DHL:5, USD:CAD:Jet1:4, USD:CAD:FEDX:6", "USD", "CAD", 10)
expected_out_2 = {"source":"USD","target":"CAD","method":"Jet1","rate":4.0,"amount_in":10.0,"amount_out":40.0}
print("direct chooses best rate:", out == expected_out_2, out)

# tie on best rate, keep first seen
out = fx.convert_direct("USD:CAD:DHL:4, USD:CAD:Jet1:4, USD:CAD:FEDX:6", "USD", "CAD", 10)
expected_out_3 = {"source":"USD","target":"CAD","method":"DHL","rate":4.0,"amount_in":10.0,"amount_out":40.0}
print("direct tie chooses first seen:", out == expected_out_3, out)

# no direct route
out = fx.convert_direct("USD:GBP:FEDX:10, EUR:USD:Jet1:2", "USD", "CAD", 10)
expected_out_4 = {"error":"No direct rate from USD to CAD"}
print("direct no route:", out == expected_out_4, out)

# case sensitive behavior
out = fx.convert_direct("Usd:Cad:Jet1:4, USD:CAD:DHL:5", "USD", "CAD", 10)
expected_out_5 = {"source":"USD","target":"CAD","method":"DHL","rate":5.0,"amount_in":10.0,"amount_out":50.0}
print("case sensitive match:", out == expected_out_5, out)



# ---------- Step 3: convert_routed ----------
fx = ForeignExchange("USD:CAD:DHL:5, USD:GBP:FEDX:10, EUR:USD:Jet1:2, GBP:JPY:DHL:7")

# simple two leg path
raw = "USD:GBP:Jet1:4, GBP:JPY:DHL:7, EUR:USD:Jet1:2"
out = fx.convert_routed(raw, "USD", "JPY", 10)
expected_route_1 = {
    "source":"USD","target":"JPY","amount_in":10.0,"total_rate":11.0,"amount_out":110.0,
    "route":{
        "currencies":["USD","GBP","JPY"],
        "methods":["Jet1","DHL"],
        "legs":[
            {"from":"USD","to":"GBP","method":"Jet1","rate":4.0},
            {"from":"GBP","to":"JPY","method":"DHL","rate":7.0},
        ]
    }
}
print("routed two leg path:", 
      out["route"]["currencies"] == expected_route_1["route"]["currencies"] and
      out["route"]["methods"] == expected_route_1["route"]["methods"] and
      abs(out["total_rate"] - expected_route_1["total_rate"]) < 1e-9 and
      abs(out["amount_out"] - expected_route_1["amount_out"]) < 1e-9,
      out)

# choose lower total rate with same hops
raw = (
    "USD:EUR:Jet1:2, EUR:CAD:DHL:2, "
    "USD:GBP:Jet2:1.5, GBP:CAD:FEDX:3.9"
)
out = fx.convert_routed(raw, "USD", "CAD", 10)
print("routed chooses lower total rate:", 
      out["route"]["currencies"] == ["USD","EUR","CAD"] and 
      abs(out["total_rate"] - 4.0) < 1e-9, 
      out)

# tie on total rate, prefer fewer hops
raw = (
    "USD:EUR:A:2, EUR:CAD:B:2, "  # total 4 with two hops
    "USD:CAD:C:4"                 # total 4 with one hop
)
out = fx.convert_routed(raw, "USD", "CAD", 10)
print("routed tie prefers fewer hops:", 
      out["route"]["currencies"] == ["USD","CAD"], out)

# no path exists
raw = "USD:EUR:A:2, JPY:CAD:B:3"
out = fx.convert_routed(raw, "USD", "CAD", 10)
print("routed no path:", out == {"error":"No path from USD to CAD"}, out)

# case sensitivity holds
raw = "Usd:EUR:A:2, EUR:CAD:B:2"
out = fx.convert_routed(raw, "USD", "CAD", 10)
print("routed case sensitive:", out == {"error":"No path from USD to CAD"}, out)

# ---------- Step 4: convert_best ----------
# direct exists and should win even if an indirect is cheaper
raw = "USD:CAD:DHL:5, USD:EUR:A:2, EUR:CAD:B:2"
out = fx.convert_best(raw, "USD", "CAD", 10)
expected_direct = {"source":"USD","target":"CAD","method":"DHL","rate":5.0,"amount_in":10.0,"amount_out":50.0}
print("best prefers direct when available:", out == expected_direct and "route" not in out, out)

# indirect used when no direct exists
raw = "USD:EUR:A:2, EUR:CAD:B:2"
out = fx.convert_best(raw, "USD", "CAD", 10)
print("best returns routed when no direct:", 
      out.get("route", {}).get("currencies") == ["USD","EUR","CAD"] and 
      abs(out.get("total_rate", 0) - 4.0) < 1e-9, 
      out)

# no path at all
raw = "USD:EUR:A:2, JPY:CAD:B:2"
out = fx.convert_best(raw, "USD", "CAD", 10)
print("best no path:", out == {"error":"No path from USD to CAD"}, out)