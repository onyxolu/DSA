class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        arrString = [str(integer) for integer in digits]
        numString = "".join(arrString)
        num = int(numString)
        num +=1
        # numString(num)
        numstring = str(num)
        print(numstring)
        for num in numstring:
            ans.append(int(num))
        return ans