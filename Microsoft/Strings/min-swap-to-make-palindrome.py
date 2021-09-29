
def CountSwap(s):
    s = list(s)
    n = len(s)
 
    # Counter to count minimum swap
    count = 0
    ans = True
 
    # A loop which run in half string
    # from starting
    for i in range(n // 2):
 
        # Left pointer
        left = i
 
        # Right pointer
        right = n - left - 1
 
        # A loop which run from right pointer
        # to left pointer
        while left < right:
 
            # if both char same then
            # break the loop if not
            # same then we have to move
            # right pointer to one step left
            if s[left] == s[right]:
                break
            else:
                right -= 1
 
        # it denotes both pointer at
        # same position and we don't
        # have sufficient char to make
        # palindrome string
        if left == right:
            ans = False
            break
        else:
            for j in range(right, n - left - 1):
                (s[j], s[j + 1]) = (s[j + 1], s[j])
                count += 1
    if ans:
        print(count)
        return (count)
    else:
        print(-1)
        return -1


CountSwap("ntiin")



# Example 1:

# Input: "mamad"
# Output: 3
# Example 2:

# Input: "asflkj"
# Output: -1
# Example 3:

# Input: "aabb"
# Output: 2
# Example 4:

# Input: "ntiin"
# Output: 1
# Explanation: swap 't' with 'i' => "nitin"