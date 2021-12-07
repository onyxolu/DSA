'''
SOLUTION:

If you take any ordinary string, and concatenate its reverse to it, you'll get a palindrome. This leads to an interesting insight about the converse: every palindrome half is reverse of the other half.

Simply speaking, if one were to start in the middle of a palindrome, and traverse outwards, they'd encounter the same characters, in the exact same order, in both halves!

Since the input string contains characters that we need to ignore in our palindromic check, it becomes tedious to figure out the real middle point of our palindromic input.

Instead of going outwards from the middle, we could just go inwards towards the middle!

So, if we start traversing inwards, from both ends of the input string, we can expect to see the same characters, in the same order.

The resulting algorithm is simple:

1. Set two pointers, one at each end of the input string

2. If the input is palindromic, both the pointers should point to equivalent characters, at all times. [1]
   If this condition is not met at any point of time, we break and return early. [2]

3. We can simply ignore non-alphanumeric characters by continuing to traverse further.

4. Continue traversing inwards until the pointers meet in the middle.

***a loop invariant is a property of a program loop that is true before (and after) each iteration.

'''

def isPalindrome(self, s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
    return True