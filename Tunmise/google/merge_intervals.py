class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []

        l = sorted(intervals,key = lambda x:x[0])

        stack = [l[0]]
        for i in l:
            last_interval = stack[-1]
            if last_interval[1] >= i[0]:
                last_interval[1] = max(last_interval[1],i[1])
                stack.pop()
                stack.append(last_interval)
            else:
                stack.append(i)
        return stack