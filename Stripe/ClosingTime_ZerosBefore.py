# Q4 Best store closing time

def store_penalty(bits: list[int], t: int) -> int:
    """
    One means a customer is present, zero means empty.
    Store is open before t, closed at and after t.
    Penalty at t equals zeros before t plus ones from t onward.
    """
    n = len(bits)
    t = max(0, min(t, n))
    zeros_before = t - sum(bits[:t])      # zeros before t
    ones_after = sum(bits[t:])            # ones from t onward
    return zeros_before + ones_after


def best_store_closing_time(bits: list[int]) -> dict:
    """
    Find t in 0..n that minimizes the penalty.
    Tie rule, choose the smallest t.
    Returns {'best_time': t, 'penalty': value} or an error object.
    """
    if not bits:
        return {"error": "no data"}
    if any(b not in (0, 1) for b in bits):
        return {"error": "non binary input"}

    n = len(bits)
    prefix_zeros = 0
    suffix_ones = sum(bits)    # ones when t equals 0

    best_t = 0
    best_penalty = prefix_zeros + suffix_ones

    for t in range(1, n + 1):
        prev = bits[t - 1]
        if prev == 0:
            prefix_zeros += 1
        else:
            suffix_ones -= 1

        penalty = prefix_zeros + suffix_ones
        if penalty < best_penalty:
            best_penalty = penalty
            best_t = t

    return {"best_time": best_t, "penalty": best_penalty}


def analyze_closing(bits: list[int]) -> dict:
    """
    Small API wrapper for callers.
    """
    return best_store_closing_time(bits)


# ========== Prints ==========

# Stage 1, penalty at a chosen close time
print("S1 [0,0,0], t=3:", store_penalty([0, 0, 0], 3), "expected 0")
print("S1 [1,1,1], t=0:", store_penalty([1, 1, 1], 0), "expected 0")
print("S1 [1,0,1], t=1:", store_penalty([1, 0, 1], 1), "expected 1")
print("S1 clamp negative t:", store_penalty([1, 0], -10), "expected 1")
print("S1 clamp large t:", store_penalty([1, 0], 99), "expected 1")

# Stage 2, best closing time
print("S2 best [0,0,0]:", best_store_closing_time([0, 0, 0]),
      "expected {'best_time': 3, 'penalty': 0}")
print("S2 best [1,1,1]:", best_store_closing_time([1, 1, 1]),
      "expected {'best_time': 0, 'penalty': 0}")
print("S2 best [1,0,1]:", best_store_closing_time([1, 0, 1]),
      "expected {'best_time': 1, 'penalty': 1}")

# Tie check, several cuts have the same minimum, choose the smallest t
print("S2 tie [0,1,0,1]:", best_store_closing_time([0, 1, 0, 1]),
      "expected {'best_time': 0, 'penalty': 2}")

# Stage 3, edge cases
print("S3 empty input:", best_store_closing_time([]),
      "expected {'error': 'no data'}")
print("S3 non binary:", best_store_closing_time([0, 2, 1]),
      "expected {'error': 'non binary input'}")

# Stage 4, API wrapper
print("S4 analyze_closing [1,0,1,1,0]:", analyze_closing([1, 0, 1, 1, 0]),
      "expected {'best_time': 1, 'penalty': 2}")
