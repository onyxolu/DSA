'''

APPROACH 1: HASHSET

One could use here the standard replace function. String consists of English lowercase letters, and hence all 26 possible duplicates are known in advance.

The idea is very simple:

Generate hashset of all 26 possible duplicates from aa to zz.

Iterate over that 26 duplicates and replace them all in string by empty char.

Note that such a strategy could introduce some new duplicates, for example abbaca -> aaca, and hence step number 2 sometimes should be repeated several times. The idea is to repeat step 2 till the string still changes after the replacements. That could be checked by the string length.

Algorithm

1. Generate hashset of all 26 possible duplicates from aa to zz.

2. Initiate 'one step before' string length by prevLength = -1.

3. While previous length is still different from the current one prevLength != S.length()

    - Set 'one step before' length to be equal to the string length prevLength = S.length().

    - Iterate over all 26 duplicates and replace them in string by empty char.

4. Return S.


Time complexity : O(N^2), where N is a string length. Here we have an onion : while -> for -> replace. while is executed not more then N/2N/2 times, for is always run 26 times, and replace has \mathcal{O}(N)O(N) run time in average. In total that results in O(N/2 * 26 N) = O(N^2)

Space complexity : O(N). The hashset of duplicates has the constant length 26, but replace function actually creates a copy of the string and thus uses O(N) space.

'''

from string import ascii_lowercase
class Solution:
    def removeDuplicates(self, S: str) -> str:
        # generate 26 possible duplicates
        duplicates = {2 * ch for ch in ascii_lowercase}
        
        prev_length = -1
        
        while prev_length != len(S):
            prev_length = len(S)
            for d in duplicates:
                S = S.replace(d, '')
                
        return S

'''

BETTER SOLUTION USING STACK

We could trade an extra space for speed. The idea is to use an output stack to keep track of only non duplicate characters. Here is how it works:

- If Current string character is equal to the last element in stack? Pop that last element out of stack.

- If Current string character is not equal to the last element in stack? Add the current character into stack.


Algorithm

1. Initiate an empty output stack.

2. Iterate over all characters in the string.

    - Current element is equal to the last element in stack? Pop that last element out of stack.

    - Current element is not equal to the last element in stack? Add the current element into stack.

3. Convert stack into string and return it.


Time complexity : O(N), where N is a string length.
Space complexity : O(N−D) where D is a total length for all duplicates.


'''

class Solution:
    def removeDuplicates(self, S: str) -> str:
        output = []
        for ch in S:
            if output and ch == output[-1]: 
                output.pop()
            else: 
                output.append(ch)
        return ''.join(output)