import collections
def cutoffRanks(scores, cutOffRank):
    count = collections.Counter(scores)
    ans, curRank = 0, 1
    for k, v in sorted(count.items(),reverse=True):
        if curRank > cutOffRank:
            break
        ans += v
        curRank += v
    return ans