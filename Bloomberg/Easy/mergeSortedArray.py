# Time Complexity = 0(N)
# Space Complexity = 0(1)

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# Three Pointers


def merge(nums1, n, nums2, m):
    last = m + n - 1 

    while m > 0 and n > 0:
        print(last, n-1, m-1)
        if nums1[m-1] > nums2[n-1]:
            nums1[last] = nums1[m-1]
            m -= 1
        else: 
            nums1[last] = nums2[n-1]
            n -= 1
        last -= 1

    # Fill nums1 with leftover of nums2
    while n > 0:
        nums1[last] = nums2[n-1]
        n -= 1
        last -= 1
    return nums1 


print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))



