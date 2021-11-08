
# Sorting in ascending order

def twoCityScheduling(costs):
    costs = sorted(costs, key = lambda x:x[0]-x[1])
    cost = 0
    for i in range(int(len(costs)/2)):
        cost += costs[i][0]
    for i in range(int(len(costs)/2), len(costs)):
        cost += costs[i][1]
    return cost

print(twoCityScheduling([[10,20],[30,200],[400,50],[30,20]]))