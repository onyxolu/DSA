def findLargest(arr) ->int:
    s = set(-a for a in arr if a <0) & set(a for a in arr if a >0)
    return max(s) if s else 0

A = [3, 2, -2, 5, -3]
B = [1, 2, 3, -4]
print(findLargest(B))