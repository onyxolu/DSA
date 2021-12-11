
from collections import List, product

# For each building, update the distance from it to all empty lands. At the end, check for all valid empty lands and get the answer.

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = [[[0, 0] for j in range(n)] for i in range(m)]
        def update(i, j):
            stack = [(i, j, 0)]
            v = set()
            v.add((i, j))
            cnt[i][j][1] -= 1
            while stack:
                a, b, steps = stack.pop(0)
                cnt[a][b][0] += steps
                cnt[a][b][1] += 1
                for c, d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    if 0 <= a + c < m and 0 <= b + d < n and (a + c, b + d) not in v and not grid[a + c][b + d]:
                        v.add((a + c, b + d))
                        stack.append((a + c, b + d, steps + 1))
        buildings = 0
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                buildings += 1
                update(i, j)
        res = float('inf')
        for i, j in product(range(m), range(n)):
            if cnt[i][j][1] == buildings:
                res = min(res, cnt[i][j][0])
        return res if res != float('inf') else -1