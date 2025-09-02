# Stage 1, extract innermost segments

# Goal
# Input is a token stream with BEGIN, END, zeros, and ones. Find only the innermost BEGIN to END spans. For each innermost span, extract the zeros and ones in order.

# Function
# extract_innermost_segments(s: str) -> list[list[int]]

# Examples

# Input, BEGIN BEGIN 0 0 1 END BEGIN 0 1 END
# Output, [[0, 0, 1], [0, 1]]

# Input, BEGIN 1 BEGIN 0 END END
# Output, [[0]]

# Unmatched END tokens are ignored. Unmatched BEGIN tokens are ignored.

# Constraints

# Preserve original left to right order of innermost segments.

# Ignore tokens that are not BEGIN, END, zero, or one.

# Time budget is linear in the number of tokens.

# Stage 2, mismatches for one segment at a chosen cut

# Goal
# Given a single segment list of zeros and ones, compute mismatches at a cut t. A mismatch is one before t, plus zero from t to the end.

# Function
# segment_mismatches(bits: list[int], t: int) -> int

# Examples

# [0, 0, 1] with t equals 2 gives 0

# [0, 1] with t equals 1 gives 0

# [1, 0, 1] with t equals 1 gives 2

# Stage 3, best cut per innermost segment

# Goal
# For each innermost segment from Stage 1, find the cut t that minimizes mismatches from Stage 2. Return a summary per segment.

# Function
# best_cut_per_innermost(s: str) -> list[dict]

# Each dict includes

# bits: the list of zeros and ones in the segment

# best_time: the chosen cut t

# mismatches: the mismatch count at that cut

# Tie rule
# If several cuts tie, choose the smallest t.



class Server:
    def __init__(self, raw_data):
        self.segments = self._parse(raw_data)

    def _parse(self, raw_data):
        tokens = raw_data.strip().split()
        stack: list[dict] = []  # each item: {"start": idx, "has_child": bool}
        results: list[list[int]] = []

        for i, tok in enumerate(tokens):
            if tok == "BEGIN":
                if stack:
                    stack[-1]["has_child"] = True
                stack.append({"start": i, "has_child": False})
            elif tok == "END":
                if not stack:
                    continue
                entry = stack.pop()
                if entry["has_child"]:
                    continue
                start = entry["start"]
                inner = tokens[start + 1 : i]
                bits = [int(x) for x in inner if x in {"0", "1"}]
                if bits:
                    results.append(bits)

        return results
    
    def mismatches(self, bits: list[int], t: int) -> int:
        """
        0 means running, 1 means offline.
        For cut t, count ones before t plus zeros from t onward.
        """
        n = len(bits)
        t = max(0, min(t, n))
        ones_before = sum(bits[:t])
        zeros_after = sum(1 for b in bits[t:] if b == 0)
        return ones_before + zeros_after
    
    def best_cut(self, segment: list[int]) -> dict:
        """
        Prefix Sum
        One pass scan that uses prefix_ones and suffix_zeros counters.
        Tie rule, choose the smallest t.
        """
        if not segment:
            return {"error": "no data"}
        
        n = len(segment)
        prefix_ones = 0
        suffix_zeros = segment.count(0)  # zeros in [0..n) when t equals 0

        best_t = 0
        best_penalty = prefix_ones + suffix_zeros  # penalty at t equals 0

        for t in range(1, n + 1):
            prev = segment[t - 1]
            if prev == 1:
                prefix_ones += 1
            else:
                suffix_zeros -= 1

            penalty = prefix_ones + suffix_zeros
            if penalty < best_penalty:
                best_penalty = penalty
                best_t = t

        return {"best_time": best_t, "mismatches": best_penalty}
    
    def best_cut_per_segment(self):
        best_cuts = []
        for segment in self.segments:
            segment = self.best_cut_per_segment(segment)
            if "error" not in segment:
                best_cuts.append(segment)
        return best_cuts
    


# ===== Q2 Stage 1, extract innermost segments =====
s1 = Server("BEGIN BEGIN 0 0 1 END BEGIN 0 1 END")
print("S1 example 1:",
      s1.segments,
      "expected [[0, 0, 1], [0, 1]]")

s2 = Server("BEGIN 1 BEGIN 0 END END")
print("S1 nested inner only:",
      s2.segments,
      "expected [[0]]")

s3 = Server("END BEGIN 0 END")
print("S1 unmatched END ignored:",
      s3.segments,
      "expected [[0]]")

s4 = Server("BEGIN 0 1")
print("S1 unmatched BEGIN ignored:",
      s4.segments,
      "expected []")

s5 = Server("BEGIN x 0 y 1 z END")
print("S1 junk tokens inside ignored:",
      s5.segments,
      "expected [[0, 1]]")

s6 = Server("BEGIN END")
print("S1 empty inner span skipped:",
      s6.segments,
      "expected []")

s7 = Server("BEGIN BEGIN 1 END END BEGIN 0 END")
print("S1 mixed nested and sibling:",
      s7.segments,
      "expected [[1], [0]]")

s8 = Server("BEGIN 0 BEGIN 1 BEGIN 0 END END END")
print("S1 deep nesting only deepest counts:",
      s8.segments,
      "expected [[0]]")


# ===== Q2 Stage 2, mismatches for a given segment and cut =====
print("S2 mismatch [0, 0, 1] at t=2:",
      s1.mismatches([0, 0, 1], 2),
      "expected 0")

print("S2 mismatch [0, 1] at t=1:",
      s1.mismatches([0, 1], 1),
      "expected 0")

print("S2 mismatch [1, 0, 1] at t=1:",
      s1.mismatches([1, 0, 1], 1),
      "expected 2")

print("S2 clamp negative t on [1, 0]:",
      s1.mismatches([1, 0], -5),
      "expected 1")

print("S2 clamp large t on [1, 0]:",
      s1.mismatches([1, 0], 100),
      "expected 1")

print("S2 empty bits at any t:",
      s1.mismatches([], 3),
      "expected 0")


# ===== Q2 Stage 3, best cut per segment =====
print("S3 best_cut on [0, 0, 1]:",
      Server("BEGIN BEGIN 0 0 1 END END").best_cut([0, 0, 1]),
      "expected {'best_time': 2, 'mismatches': 0}")

print("S3 best_cut on [1, 0, 1, 0]:",
      Server("BEGIN 1 0 1 0 END").best_cut([1, 0, 1, 0]),
      "expected {'best_time': 0, 'mismatches': 2}")

srv_multi = Server("BEGIN BEGIN 0 0 1 END BEGIN 0 1 END")
print("S3 best_cut_per_segment, two segments:",
      srv_multi.best_cut_per_segment(),
      "expected [{'bits': [0, 0, 1], 'best_time': 2, 'mismatches': 0}, {'bits': [0, 1], 'best_time': 1, 'mismatches': 0}]")

srv_none = Server("BEGIN END")
print("S3 best_cut_per_segment when no segments:",
      srv_none.best_cut_per_segment(),
      "expected []")
