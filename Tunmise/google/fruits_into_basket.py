class Solution:
    def totalFruit(self, fruits) -> int:

        start =0 
        end = 0
        d = {}
        max_val = 0
        while end < len(fruits):
            d[fruits[end]] = end
            if len(d) >=3:
                min_val = min(d.values())
                del d[fruits[min_val]]
                start = min_val +1 

            max_val = max(max_val,end -start +1)
            end += 1
        return max_val