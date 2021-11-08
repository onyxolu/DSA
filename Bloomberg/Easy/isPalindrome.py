# Time Complexity = 0(N)
# Space Complexity = 0(1)


def isPalindrome(self, s: str) -> bool:
    clean_str = ""
    for val in s:
        if val.isalnum():
            clean_str += val.lower()
    # return clean_str == clean_str[::-1]
    left = 0
    right = len(clean_str) -1
    for val in clean_str:
        if clean_str[left] != clean_str[right]:
            return False
        left +=1
        right -= 1
    return True


def isPalindrome(self, s: str) -> bool:
    clean_str = ""
    for val in s:
        if val.isalnum():
            clean_str += val.lower()
    return clean_str == clean_str[::-1]
