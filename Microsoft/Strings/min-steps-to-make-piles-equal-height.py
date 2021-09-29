from collections import Counter
def minStepEqualPiles(A):
    cnt = Counter(A)
    nums = sorted(cnt.keys(), reverse=True)
    k, ans = 0, 0
    for x in nums[:-1]:
        k += cnt[x]
        ans += k
    return ans

# A = [5, 2, 1]
# B = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4]
# print(minStepEqualPiles(B))

# A = [4, 5, 5, 4, 2]
# print(minStepEqualPiles(A))


from typing import List


def min_steps_balance(piles: List[int]) -> int:
    """
    Time  : O(N log N)
    Space : O(1), where N = len(s)
    """

    # EDGE CASE
    if len(piles) < 2:
        return 0

    # SORT THE BLOCKS
    piles = sorted(piles, reverse=True)

    # COUNT THE STEPS WE NEED
    steps = 0

    # EACH TIME WE SEE A DIFFERENT ELEMENT, WE NEED TO SEE HOW MANY ELEMENTS ARE BEFORE IT
    for i in range(1, len(piles)):
        steps += i if piles[i - 1] != piles[i] else 0

    return steps


print(min_steps_balance([1, 1, 2, 2, 2, 3, 3, 3, 4, 4]) == 15)

