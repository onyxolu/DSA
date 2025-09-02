# Partners send us a pricing table that mixes countries, carriers, and rules. The table is mostly clean, sometimes it has gaps, sometimes the same product has different prices in different places. A merchant gives us an order made of line items with product ids and quantities, plus a ship to country. We need to return numbers they can trust, fast, and with a clear explanation of how we got there.

# We will build this in four steps.

# Step 1, parse pricing data

# You receive a JSON like structure as a string. It maps country to carriers, each carrier has product level prices. Some entries can be missing, skip or record them, but be consistent and explain your choice.

# Input

# {
#   "US": {
#     "DHL":  { "p1": 5.00, "p2": 7.50 },
#     "FedEx":{ "p1": 6.00 }
#   },
#   "EU": {
#     "DHL":  { "p1": 4.50, "p3": 8.00 },
#     "Jet1": { "p2": 6.75, "p3": 7.25 }
#   }
# }


# Expectation

# Produce a structure you can query quickly by country, then carrier, then product id, then unit shipping price.

# Ignore entries where the unit price is not a number; keep order where possible.

# If a country or carrier is missing for a requested product you will handle it later.

# Step 2, compute shipping for an order with a chosen carrier

# Given a country, a carrier, and an order that lists product ids and quantities, compute the total shipping cost, sum of quantity times unit shipping price for that carrier. If a product has no price for that carrier in that country, decide a policy and state it, either skip the line or return an error.


# Edge case to test: product not priced for that carrier in that country.

# Step 3, add tiered pricing by quantity

# Some carriers offer breaks when quantity meets a threshold for a single product line. For example, for DHL in EU, p3 costs 8.00 per unit for qty less than 5, then 7.00 per unit for qty at least 5. Add support for simple tiers at the product level. If a tier is missing, use the base unit price.

# Updated pricing input for EU

# Step 4, choose the cheapest carrier for the order

# If the order does not specify a carrier, evaluate all carriers available for the country, apply tier rules, skip carriers that cannot price every line under your policy, and return the cheapest option. Include a short breakdown so the result is explainable.

raw_pricing = """
{
  "US": {
    "DHL":  { "p1": 5.00, "p2": 7.50 },
    "FedEx":{ "p1": 6.00 }
  },
  "EU": {
    "DHL":  { "p1": 4.50, "p3": 8.00 },
    "Jet1": { "p2": 6.75, "p3": 7.25 }
  }
}
"""

# country => method => product

import json
from typing import Any, Dict, List, Optional, Tuple

class Shipping:
    def __init__(self, costs):
        self.costs = self._parse(costs)

    def _parse(self, cost_json):
        try:
            costs = json.loads(cost_json)
        except json.JSONDecodeError as e:
            print("Invalid JSON:", e)
            
        print(costs)
        return costs
    
    def get_cost(self, country: str, method: str, product_id: str) -> dict:
        # Lookup by country
        country_data = self.costs.get(country)
        if not country_data:
            return {"error": f"No data for country {country}"}
        
        # Lookup by method
        method_data = country_data.get(method)
        if not method_data:
            return {"error": f"No data for method {method} in country {country}"}
        
        # Lookup by product
        cost = method_data.get(product_id)
        if cost is None:
            return {"error": f"No data for product {product_id} in {country} with {method}"}
        
        # Success
        return {
            "country": country,
            "method": method,
            "product": product_id,
            "cost": cost
        }

    # ---------- Step 3: tiered pricing ----------
    def _resolve_unit_price(self, country: str, method: str, product_id: str, qty: int) -> Tuple[Optional[float], Optional[str]]:
        """
        Returns (unit_price, note). note is a short string when a tier is applied.
        """
        base = self.costs.get(country, {}).get(method, {}).get(product_id)
        if base is None:
            return None, None

        # Plain number
        if isinstance(base, (int, float)):
            return float(base), None

        # Tiered form
        if isinstance(base, dict):
            tiers = base.get("tiers")
            if not isinstance(tiers, list) or not tiers:
                # Try a fallback base price if present, else no price
                if "unit" in base and isinstance(base["unit"], (int, float)):
                    return float(base["unit"]), None
                return None, None

            # Filter valid tiers and sort by min_qty ascending
            clean_tiers = []
            for t in tiers:
                if not isinstance(t, dict):
                    continue
                mq = t.get("min_qty")
                unit = t.get("unit")
                if isinstance(mq, int) and mq >= 1 and isinstance(unit, (int, float)):
                    clean_tiers.append((mq, float(unit)))
            if not clean_tiers:
                return None, None
            clean_tiers.sort(key=lambda x: x[0])

            # Pick the highest min_qty that is <= qty
            chosen = None
            for mq, unit in clean_tiers:
                if qty >= mq:
                    chosen = (mq, unit)
            if chosen is None:
                # qty below the smallest tier min_qty; if a base unit present, use it, else no price
                smallest_mq, smallest_unit = clean_tiers[0]
                if smallest_mq == 1:
                    return smallest_unit, None
                return None, None

            mq, unit = chosen
            return unit, f"tier applied: min_qty {mq} unit {unit:.2f}"

        # Unknown shape
        return None, None

    def price_order_for_carrier(self, order: dict) -> dict:
        """
        order = {
          "country": "EU",
          "carrier": "DHL",
          "items": [ {"product_id":"p3","qty":6}, ... ]
        }
        """
        country = order.get("country")
        carrier = order.get("carrier")
        items = order.get("items", [])

        if not country or not carrier or not isinstance(items, list):
            return {"error": "Order must include country, carrier, and items list"}

        lines: list[dict] = []
        notes: list[str] = []
        total = 0.0

        for it in items:
            pid = it.get("product_id")
            qty = it.get("qty")
            if not pid or not isinstance(qty, int) or qty <= 0:
                return {"error": f"Invalid item {it}"}

            unit, note = self._resolve_unit_price(country, carrier, pid, qty)
            if unit is None:
                return {"error": f"No price for product {pid} in {country} with {carrier}"}

            line_total = unit * qty
            line_entry = {"product_id": pid, "unit": round(unit, 2), "qty": qty, "line_total": round(line_total, 2)}
            lines.append(line_entry)
            total += line_total
            if note:
                notes.append(note)

        result = {
            "country": country,
            "carrier": carrier,
            "lines": lines,
            "total": round(total, 2)
        }
        if notes:
            result["notes"] = sorted(set(notes))  # dedupe, stable enough
        return result


# =========================
# Print style tests for Shipping
# =========================

# ---------- Fixtures ----------
raw_pricing_step1 = """
{
  "US": {
    "DHL":  { "p1": 5.00, "p2": 7.50 },
    "FedEx":{ "p1": 6.00 }
  },
  "EU": {
    "DHL":  { "p1": 4.50, "p3": 8.00 },
    "Jet1": { "p2": 6.75, "p3": 7.25 }
  }
}
"""

# malformed JSON, trailing comma
raw_bad_json = """
{
  "US": {
    "DHL":  { "p1": 5.00, "p2": 7.50 },
  }
}
"""

raw_pricing_tiered = """
{
  "EU": {
    "DHL":  {
      "p1": 4.50,
      "p3": { "tiers": [ { "min_qty": 1, "unit": 8.00 }, { "min_qty": 5, "unit": 7.00 } ] }
    },
    "Jet1": { "p2": 6.75, "p3": 7.25 }
  },
  "US": {
    "FedEx": { "p1": 6.00, "p2": 7.50 }
  }
}
"""

# ---------- Step 1: parsing ----------

# happy path
ship1 = Shipping(raw_pricing_step1)
print("parse keeps top level countries:", all(k in ship1.costs for k in ["US", "EU"]))
print("parse keeps US methods:", all(k in ship1.costs["US"] for k in ["DHL", "FedEx"]))
print("parse keeps EU DHL products:", all(k in ship1.costs["EU"]["DHL"] for k in ["p1", "p3"]))
print("parse correct numeric leaf, US DHL p1:", ship1.costs["US"]["DHL"]["p1"])

# malformed JSON should raise or be handled
raised = False
try:
    Shipping(raw_bad_json)
except Exception as e:
    raised = True
print("malformed JSON is rejected:", raised)

# ---------- Step 2: direct lookup ----------

ship2 = Shipping(raw_pricing_step1)

resp = ship2.get_cost("US", "DHL", "p1")
print("lookup US DHL p1:", resp)

resp = ship2.get_cost("US", "FedEx", "p1")
print("lookup US FedEx p1:", resp)

resp = ship2.get_cost("EU", "Jet1", "p3")
print("lookup EU Jet1 p3:", resp)

resp = ship2.get_cost("EU", "Jet1", "pX")
print("unknown product returns error:", resp)

resp = ship2.get_cost("ASIA", "DHL", "p1")
print("unknown country returns error:", resp)

resp = ship2.get_cost("US", "UPS", "p1")
print("unknown method returns error:", resp)

# ---------- Step 3: tiered pricing and order pricing ----------

ship3 = Shipping(raw_pricing_tiered)

# single line where tier applies
order1 = {
  "country": "EU",
  "carrier": "DHL",
  "items": [ {"product_id": "p3", "qty": 6} ]
}
resp = ship3.price_order_for_carrier(order1)
print("tiered unit 7.00 for qty 6 gives total and lines:", resp)

# mixed lines, one flat one tiered
order2 = {
  "country": "EU",
  "carrier": "DHL",
  "items": [
    {"product_id": "p1", "qty": 2},
    {"product_id": "p3", "qty": 6}
  ]
}
resp2 = ship3.price_order_for_carrier(order2)
print("two line order total and breakdown:", resp2)

# invalid item qty
bad_order = {
  "country": "EU",
  "carrier": "DHL",
  "items": [ {"product_id": "p3", "qty": 0} ]
}
resp_bad = ship3.price_order_for_carrier(bad_order)
print("invalid qty returns error:", resp_bad)

# missing price for a product under a carrier
missing_price_order = {
  "country": "EU",
  "carrier": "Jet1",
  "items": [ {"product_id": "p1", "qty": 1} ]  # Jet1 has no p1 in EU
}
resp_missing = ship3.price_order_for_carrier(missing_price_order)
print("missing price returns error:", resp_missing)
