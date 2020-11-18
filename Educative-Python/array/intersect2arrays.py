def intersect1(nums1, nums2):
    intersect = set(nums1).intersection(nums2)
    ans = []
    for val in intersect:
        ans.append(val)
    print("intersect1")
    return ans

def intersect2(nums1, nums2):
    ans = []
    for num in nums1:
        if num in nums2:
            if not num in ans:
                ans.append(num)
    print("intersect2")
    return ans

print(intersect2([1,2,2,1], [2,2]))
print(intersect1([1,2,2,1], [2,2]))         