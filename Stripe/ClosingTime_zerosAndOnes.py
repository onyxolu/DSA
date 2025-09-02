

# Stage 1, compute mismatches at a chosen cut

# Goal
# You get a string of server statuses, tokens are 0 and 1 separated by spaces. Zero means running, one means offline. For a chosen cut time t, the server is considered offline from index t to the end. Count the mismatches at time t. A mismatch is one before t, or zero at or after t.

# Function
# mismatches(status_line: str, t: int) -> int

# Examples

# Input, "1 0 0 1", t equals 2, Output, 1
# Explanation, ones before t equals positions 0 and 1 gives 1, zeros after t equals positions 2 and 3 gives 0, total equals 1.

# Input, "0 0 0", t equals 0, Output, 3

# Input, "1 1 1", t equals 3, Output, 2

# Constraints

# Indices are zero based.

# If t is outside the array, clamp to the array bounds.

# Time limit is one pass where possible, memory should be small.

# You may ask

# Should non digit tokens be ignored or treated as errors

# Are empty strings allowed

# Stage 2, find the best cut

# Goal
# Find the cut time t in the range zero through n that gives the smallest mismatch count from Stage 1. Return both the best t and the mismatch count.

# Function
# best_cut(status_line: str) -> { "best_time": int, "mismatches": int }

# Tie rule
# If several cuts give the same minimum, choose the smallest t.

# Examples

# "1 0 0 1" gives {"best_time": 2, "mismatches": 1}

# "0 0 0" gives {"best_time": 3, "mismatches": 0}

# "1 1 1" gives {"best_time": 0, "mismatches": 0}


class Server:
    def __init__(self, raw_bits):
        self.bits = self._parse_bits(raw_bits)

    def _parse_bits(self, raw_bits: str) -> list[int]:
        return [int(tok) for tok in raw_bits.strip().split() if tok in {"0", "1"}]
    
    def clean_customers_line(s: str) -> list[int]:
        """
        Map common truthy and falsy tokens to 1 or 0.
        Ignore anything else, keep order.
        """
        truthy = {"1", "y", "yes", "true", "t"}
        falsy = {"0", "n", "no", "false", "f"}
        out: list[int] = []
        for tok in s.split():
            low = tok.lower()
            if low in truthy:
                out.append(1)
            elif low in falsy:
                out.append(0)
        return out

    def mismatches(self, t: int) -> int:
        """
        0 means running, 1 means offline.
        For cut t, count ones before t plus zeros from t onward.
        """
        n = len(self.bits)
        t = max(0, min(t, n))
        ones_before = sum(self.bits[:t])
        zeros_after = sum(1 for b in self.bits[t:] if b == 0)
        return ones_before + zeros_after
    
    def best_cut(self) -> dict:
        """
        Prefix Sum
        One pass scan that uses prefix_ones and suffix_zeros counters.
        Tie rule, choose the smallest t.
        """
        if not self.bits:
            return {"error": "no data"}
        
        n = len(self.bits)
        prefix_ones = 0
        suffix_zeros = self.bits.count(0)  # zeros in [0..n) when t equals 0

        best_t = 0
        best_penalty = prefix_ones + suffix_zeros  # penalty at t equals 0

        for t in range(1, n + 1):
            prev = self.bits[t - 1]
            if prev == 1:
                prefix_ones += 1
            else:
                suffix_zeros -= 1

            penalty = prefix_ones + suffix_zeros
            if penalty < best_penalty:
                best_penalty = penalty
                best_t = t

        return {"best_time": best_t, "mismatches": best_penalty}


# ========== Step 1 prints: mismatches ==========
print("mismatches basic t=2 on '1 0 0 1':",
      Server("1 0 0 1").mismatches(2), "expected 2")

print("mismatches basic t=3 on '1 0 0 1':",
      Server("1 0 0 1").mismatches(3), "expected 1")

print("mismatches all zeros t=0:",
      Server("0 0 0").mismatches(0), "expected 3")

print("mismatches all ones t=3:",
      Server("1 1 1").mismatches(3), "expected 3")

print("mismatches clamp low t negative on '1 0':",
      Server("1 0").mismatches(-5), "expected 1")

print("mismatches clamp high t too large on '1 0':",
      Server("1 0").mismatches(100), "expected 1")

print("mismatches empty input:",
      Server("").mismatches(2), "expected 0")

# ========== Step 2 prints: best_cut ==========
print("best on '1 0 0 1':",
      Server("1 0 0 1").best_cut(),
      "expected {'best_time': 3, 'mismatches': 1}")

print("best on all zeros:",
      Server("0 0 0").best_cut(),
      "expected {'best_time': 3, 'mismatches': 0}")

print("best on all ones:",
      Server("1 1 1").best_cut(),
      "expected {'best_time': 0, 'mismatches': 0}")

print("tie pick smallest t on '0 1 0 1':",
      Server("0 1 0 1").best_cut(),
      "expected {'best_time': 1, 'mismatches': 1}")

print("best with junk tokens kept out:",
      Server("a 1  b 0  1  x").best_cut(),
      "expected {'best_time': 0, 'mismatches': 1}")

print("best with tabs as separators:",
      Server("1\t0\t1").best_cut(),
      "expected {'best_time': 0, 'mismatches': 1}")

print("best on single zero:",
      Server("0").best_cut(),
      "expected {'best_time': 1, 'mismatches': 0}")

print("best on single one:",
      Server("1").best_cut(),
      "expected {'best_time': 0, 'mismatches': 0}")

print("best on empty input:",
      Server("").best_cut(),
      "expected {'error': 'no data'}")
