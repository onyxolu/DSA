'''

APPROACH 1: FOLLOW THE RULES

We can simply check if the string follows all the rules, and we can break the rules into groups.

1. Digits (one of ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    Both decimal numbers and integers must contain at least one digit.

2. A sign ("+" or "-")
    Sign characters are optional for both decimal numbers and integers, but if one is present, it will always be the first character. Note, this means that a sign character can also appear immediately after an exponent.

3. An exponent ("e" or "E")
    Exponents are also optional, but if the string contains one then it must be after a decimal number or an integer.

4. An integer must follow the exponent.
    A dot (".")

5. A decimal number should only contain one dot. Integers cannot contain dots.
    Anything else

6. There will never be anything else in a valid number.


Algorithm

Now that we have laid out the rules, let's iterate over the input. For each character, determine what group it belongs to, and verify that it follows the rules.

1. Declare 3 variables seenDigit, seenExponent, and seenDot. Set all of them to false.

2. Iterate over the input.

3. If the character is a digit, set seenDigit = true.

4. If the character is a sign, check if it is either the first character of the input, or if the character before it is an exponent. If not, return false.

5. If the character is an exponent, first check if we have already seen an exponent or if we have not yet seen a digit. If either is true, then return false. Otherwise, set seenExponent = true, and seenDigit = false. We need to reset seenDigit because after an exponent, we must construct a new integer.

6. If the character is a dot, first check if we have already seen either a dot or an exponent. If so, return false. Otherwise, set seenDot = true.

7. If the character is anything else, return false.

8. At the end, return seenDigit. This is one reason why we have to reset seenDigit after seeing an exponent - otherwise an input like "21e" would be incorrectly judged as valid.


'''


class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_exponent = seen_dot =  False
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ["+", "-"]:
                if i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
            elif c in ["e", "E"]:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif c == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False
        
        return seen_digit


'''

Time complexity: O(N), where N is the length of s.

We simply iterate over the input once. The number of operations we perform for each character in the input is independent of the length of the string, and therefore only requires constant time. This results in N . O(1) = O(N)

Space complexity - O(1) - Regardless of the input size, we only store 3 variables, seenDigit, seenExponent, and seenDot.

'''