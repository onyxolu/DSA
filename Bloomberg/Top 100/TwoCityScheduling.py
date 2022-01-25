
# Sorting in ascending order
# opportunity cost (choose A you give up B)

def twoCityScheduling(costs):
    costs = sorted(costs, key=lambda x: x[0]-x[1])
    # So the cheaper costs for A are at the beginning and the more cost ones at the end
    # sending a person to city A, the company will loose amount A-B and vice versa
    print(costs)
    cost = 0
    for i in range(int(len(costs)/2)):
        cost += costs[i][0]
    for i in range(int(len(costs)/2), len(costs)):
        cost += costs[i][1]
    return cost


print(twoCityScheduling([[10, 20], [30, 200], [400, 50], [30, 20]]))


# class Solution:
#     def twoCitySchedCost(self, costs: List[List[int]]) -> int:
#         # Sort by a gain which company has
#         # by sending a person to city A and not to city B
#         costs.sort(key = lambda x : x[0] - x[1])

#         total = 0
#         n = len(costs) // 2
#         # To optimize the company expenses,
#         # send the first n persons to the city A
#         # and the others to the city B
#         for i in range(n):
#             total += costs[i][0] + costs[i + n][1]
#         return total
