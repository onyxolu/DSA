# You receive an array of strings. Each string contains a timestamp at the start, then some fields, then a masked credit card, all separated by spaces. The timestamp is not a common format. The array is unsorted. You need to normalize the records, sort them by the timestamp, and produce a cleaned output. Later you will add small transformations and a speed pass.

# We will do this in four steps.

# Step 1, parse

# Given an array of lines, extract fields by position. The first field is a time token that sorts lexicographically after normalization. Some lines have extra spaces. Some have missing fields. Keep only rows that you can parse without guessing. Preserve the original order of kept rows for now.

# Example input

# [
#   "9|2025-01-01T10:00:00Z txn_1234 4242****4242 AUTH OK",
#   "10|2025-01-01T09:59:59Z txn_1001 4000****0002 CAPTURE FAIL",
#   "2|2025-01-01T10:00:00Z   txn_0001   4111****1111 AUTH OK",
#   "badrow without enough parts",
#   "11|2025-01-01T09:59:58Z txn_1002 4242****4242 REFUND OK"
# ]


# Notes

# The left token before the bar is a sequence that you will use as part of sort key later

# After the bar is an ISO time

# Then an id, then a masked card, then a type like AUTH or CAPTURE or REFUND, then a status like OK or FAIL


# Step 2 — Sorting and Basic Formatting

# After parsing, the records are sorted using a stable key. The sort key is (iso_time, seq, raw_index). This ensures chronological order first, then sequence number, and finally original position if ties occur. The output at this stage is a simple formatted string view of each record:

# [iso_time] [txn_id] [kind] [status]


# No transformations are applied yet, you just get them in the right order with consistent spacing.

# Step 3 — Transformations

# Here you apply transformations to make the records safer and easier to consume:

# Card redaction: Keep only the last four digits of the masked card, replace the rest with ****.

# Kind mapping: Convert transaction types like AUTH, CAPTURE, REFUND into single-letter codes (A, C, R).

# Status normalization: Force status values like ok or fail into uppercase (OK, FAIL).

# At this stage you still hold all fields, but they are transformed versions of the parsed data.

# Step 4 — Final Cleaned Output

# Now you produce the final subject-line style strings that can be used directly in reports or notifications. The format is:

# [iso_time] [txn_id] [kind_code] [status_up]


# If the status is FAIL, you prefix the line with a marker (default "FAIL "). This makes error cases stand out. The output is a clean, sorted, and transformed list of strings ready for external consumption.

sample_data = [
  "9|2025-01-01T10:00:00Z txn_1234 4242****4242 AUTH OK",
  "10|2025-01-01T09:59:59Z txn_1001 4000****0002 CAPTURE FAIL",
  "2|2025-01-01T10:00:00Z   txn_0001   4111****1111 AUTH OK",
  "badrow without enough parts",
  "bad row without enough parts",
  "11|2025-01-01T09:59:58Z txn_1002 4242****4242 REFUND OK"
]


class Transactions:
    def __init__(self, raw_data: list[str]):
        self.transactions = self._parse(raw_data)

    def _parse(self, raw_data: list[str]):
        parsed_list = []
        for idx, trans in enumerate(raw_data):
            tokens = trans.split()
            if len(tokens) != 5:
                continue
            time_and_sequence = tokens[0]
            if "|" not in time_and_sequence:
                continue
            seq_str, time_str = time_and_sequence.split("|", 1)
            try:
                seq = int(seq_str)
            except ValueError:
                continue
            parsed_list.append({
                "seq": seq,
                "iso_time": time_str.strip(),
                "txn_id": tokens[1].strip(),
                "card_mask": tokens[2].strip(),
                "kind": tokens[3].strip(),
                "status": tokens[4].strip(),
                "raw_index": idx
            })
        return parsed_list
    
    def _get_sorted_transactions(self):
        rows = self.transactions
        sorted_rows = sorted(
                        rows,
                        key=lambda r: (r["iso_time"], r["seq"], r["raw_index"])
                    )
        return [f'{r["iso_time"]} {r["txn_id"]} {r["kind"]} {r["status"]}' for r in sorted_rows]


    # ---- Step 3 helpers ----
    def _redact_card(self, card_mask: str) -> str:
        """Keep only the last four digits, redact the rest."""
        digits = "".join(ch for ch in card_mask if ch.isdigit())
        last4 = digits[-4:] if len(digits) >= 4 else digits
        return f"****{last4}"

    def _map_kind(self, kind: str) -> str:
        """Map to a short code."""
        table = {
            "AUTH": "A",
            "CAPTURE": "C",
            "REFUND": "R",
            "VOID": "V",
            "SALE": "S",
        }
        return table.get(kind.upper(), kind[:1].upper() or "?")

    def _transform_record(self, r: dict) -> dict:
        """Apply transforms without changing the original record."""
        return {
            "seq": r["seq"],
            "iso_time": r["iso_time"],
            "txn_id": r["txn_id"],
            "card_redacted": self._redact_card(r["card_mask"]),
            "kind_code": self._map_kind(r["kind"]),
            "status_up": r["status"].upper(),
            "raw_index": r["raw_index"],
        }

    def format_subject_lines_transformed(self, prefix_fail: str = "FAIL ") -> list[str]:
        """
        Sort first, then transform, then format.
        Subject line format:
          "[iso_time] [txn_id] [kind_code] [status_up]"
        If status is FAIL, prefix the line with prefix_fail.
        """
        rows = sorted(self.transactions, key=lambda r: (r["iso_time"], r["seq"], r["raw_index"]))
        out: list[str] = []
        for r in rows:
            t = self._transform_record(r)
            line = f'{t["iso_time"]} {t["txn_id"]} {t["kind_code"]} {t["status_up"]}'
            if t["status_up"] == "FAIL":
                line = prefix_fail + line
            out.append(line)
        return out


# =========================
# Print style tests for Steps 1 to 4
# =========================

print("\n--- Step 1: parse ---")
tx = Transactions(sample_data)
expected_parsed = [
    {
        "seq": 9,
        "iso_time": "2025-01-01T10:00:00Z",
        "txn_id": "txn_1234",
        "card_mask": "4242****4242",
        "kind": "AUTH",
        "status": "OK",
        "raw_index": 0
    },
    {
        "seq": 10,
        "iso_time": "2025-01-01T09:59:59Z",
        "txn_id": "txn_1001",
        "card_mask": "4000****0002",
        "kind": "CAPTURE",
        "status": "FAIL",
        "raw_index": 1
    },
    {
        "seq": 2,
        "iso_time": "2025-01-01T10:00:00Z",
        "txn_id": "txn_0001",
        "card_mask": "4111****1111",
        "kind": "AUTH",
        "status": "OK",
        "raw_index": 2
    },
    {
        "seq": 11,
        "iso_time": "2025-01-01T09:59:58Z",
        "txn_id": "txn_1002",
        "card_mask": "4242****4242",
        "kind": "REFUND",
        "status": "OK",
        "raw_index": 5
    },
]
print("kept rows count:", len(tx.transactions) == len(expected_parsed))
print("first kept row ok:", tx.transactions[0] == expected_parsed[0])

print("\n--- Step 2: sort and basic formatting ---")
expected_sorted = [
    "2025-01-01T09:59:58Z txn_1002 REFUND OK",
    "2025-01-01T09:59:59Z txn_1001 CAPTURE FAIL",
    "2025-01-01T10:00:00Z txn_0001 AUTH OK",
    "2025-01-01T10:00:00Z txn_1234 AUTH OK",
]
basic_sorted = tx._get_sorted_transactions()
print("sorted view matches:", basic_sorted == expected_sorted, basic_sorted)

print("\n--- Step 3: transform card ---")
transformed = [tx._transform_record(r) for r in tx.transactions]
card_samples = [t["card_redacted"] for t in transformed]
expected_cards = ["****4242", "****0002", "****1111", "****4242"]
print("card redaction applied:", card_samples == expected_cards, card_samples)

print("\n--- Step 4: combined cleaned output ---")
expected_subjects = [
    "2025-01-01T09:59:58Z txn_1002 R OK",
    "FAIL 2025-01-01T09:59:59Z txn_1001 C FAIL",
    "2025-01-01T10:00:00Z txn_0001 A OK",
    "2025-01-01T10:00:00Z txn_1234 A OK",
]
subjects = tx.format_subject_lines_transformed()
print("transformed subjects match:", subjects == expected_subjects, subjects)
