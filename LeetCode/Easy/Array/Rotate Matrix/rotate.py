class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        result = []

          # initialize result array
        for i in range(l):
            
            result.append([])


        for i, v in enumerate(matrix[::-1]):
            for j in range(l):
              result[j].append(v[j])
        print(result)

        for i in range(l):
            
            matrix[i] = result[i]