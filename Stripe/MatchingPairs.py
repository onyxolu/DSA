# Q6. Matching pairs in an array
# Stage 1, find any valid pair

# Goal
# Given an array of integers and a target sum, return one pair of indices whose values add to the target. Use zero based indices.

# Function
# find_one_pair(nums: list[int], target: int) -> tuple[int, int] | { "error": str }

# Rules

# If several pairs exist, return the one with the smallest first index, then the smallest second index.

# If no pair exists, return an error object.

# Time target is linear on average, memory is small.

# Examples

# nums = [1, 2, 3, 4], target = 5 returns (0, 3)

# nums = [2, 2, 3], target = 4 returns (0, 1)

# nums = [1, 1, 1], target = 10 returns an error

# Stage 2, return all disjoint pairs

# Goal
# Return a set of disjoint index pairs where each pair sums to the target. Each index can be used at most once. Prefer the earliest available indices when forming pairs.

# Function
# disjoint_two_sum_pairs(nums: list[int], target: int) -> list[tuple[int, int]]

# Rules

# Build pairs left to right. When you see a value that completes a waiting value, pair it with the earliest waiting index.

# Return pairs sorted by the first index, then the second.

# If no pairs exist, return an empty list.

# Examples

# nums = [1, 2, 3, 2, 3, 4], target = 5 returns [(1, 5), (2, 4)]

# nums = [2, 2, 2, 3, 3], target = 5 returns [(0, 3), (1, 4)]

# nums = [1, 1, 1], target = 3 returns []

# Stage 3, tie rules and edge cases

# Goal
# Lock in behavior for tricky inputs and document it.

# Tie rules

# When multiple earlier indices can pair with the current value, choose the smallest waiting index.

# When multiple equal value pairs are possible, the left to right build order determines the result.

# Sorting at the end is by first index, then second.

# Edge cases

# Negative numbers are allowed and should work.

# Repeated values are allowed.

# Empty input returns an empty list.

# Very long input should complete in linear time with queues per value.

# You may ask

# Should the result allow pairs like (i, i) if 2 * nums[i] == target

# Do we need to cap the number of pairs returned

# What are the memory constraints

# Stage 4, API shape and tests

# Goal
# Wrap the logic behind a simple API and list the tests you would run.

# Function
# analyze_pairs(nums: list[int], target: int) -> { "pairs": list[tuple[int, int]] }


from collections import defaultdict, deque
from typing import List, Tuple, Dict, Union

# ========== Stage 1, find one valid pair ==========

def find_one_pair(nums: List[int], target: int) -> Union[Tuple[int, int], Dict[str, str]]:
    """
    Return one index pair whose values sum to target.
    Tie rule, smallest first index, then smallest second index.
    """
    earliest: Dict[int, int] = {}  # value -> earliest index
    for i, v in enumerate(nums):
        need = target - v
        if need in earliest:
            j = earliest[need]
            return (j, i)
        if v not in earliest:
            earliest[v] = i
    return {"error": "no pair"}


# ========== Stage 2, return all disjoint pairs ==========

def disjoint_two_sum_pairs(nums: List[int], target: int) -> List[Tuple[int, int]]:
    """
    Build disjoint pairs, prefer earliest indices.
    When a value arrives, if someone is waiting for it, pair with the earliest waiter.
    Else, add this index to the wait list for its needed partner.
    """
    waiting: Dict[int, deque] = defaultdict(deque)  # value we need -> queue of indices waiting for it
    pairs: List[Tuple[int, int]] = []

    for i, v in enumerate(nums):
        if waiting[v]:
            j = waiting[v].popleft()
            pairs.append((j, i))
        else:
            need = target - v
            waiting[need].append(i)

    pairs.sort(key=lambda p: (p[0], p[1]))
    return pairs


# ========== Stage 3, edge cases and tie rules are covered by the logic above ==========

def analyze_pairs(nums: List[int], target: int) -> Dict[str, List[Tuple[int, int]]]:
    """
    Small API wrapper.
    """
    return {"pairs": disjoint_two_sum_pairs(nums, target)}





# ========== Print checks ==========

# Stage 1
print("S1 basic:",
      find_one_pair([1, 2, 3, 4], 5),
      "expected (0, 3)")

print("S1 duplicates:",
      find_one_pair([2, 2, 3], 4),
      "expected (0, 1)")

print("S1 no pair:",
      find_one_pair([1, 1, 1], 10),
      "expected {'error': 'no pair'}")

print("S1 tie rule smallest first index:",
      find_one_pair([3, 1, 2, 2], 5),
      "expected (0, 2)")

# Stage 2
print("S2 disjoint, simple:",
      disjoint_two_sum_pairs([1, 2, 3, 2, 3, 4], 5),
      "expected [(1, 5), (2, 4)]")

print("S2 disjoint, many repeats:",
      disjoint_two_sum_pairs([2, 2, 2, 3, 3], 5),
      "expected [(0, 3), (1, 4)]")

print("S2 disjoint, none:",
      disjoint_two_sum_pairs([1, 1, 1], 3),
      "expected []")

print("S2 negatives work:",
      disjoint_two_sum_pairs([-1, 2, -2, 3, 1, 0], 1),
      "expected [(0, 4), (2, 3)]")

print("S2 equal numbers with target twice value:",
      disjoint_two_sum_pairs([5, 5, 5, 5], 10),
      "expected [(0, 1), (2, 3)]")

# Stage 3 edge behavior via Stage 2
print("S3 tie earliest waiter wins:",
      disjoint_two_sum_pairs([1, 4, 2, 3, 2], 5),
      "expected [(0, 1), (2, 3)]")

# Stage 4
print("S4 analyze wrapper:",
      analyze_pairs([1, 2, 3, 2, 3, 4], 5),
      "expected {'pairs': [(1, 5), (2, 4)]}")

