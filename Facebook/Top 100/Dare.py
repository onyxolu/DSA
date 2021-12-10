
"""

You are given 3 arrays, merge all three arrays into one single array and return it

arr1 = [2,4,5,7]
arr2 = [1,2,4,5,6]
arr3 = [3,5,6,7,9]

        aptr = 2  1
        bptr = 2  2
        cptr = 3  0
        
        1 1 1
        1 1 1
        1 1 1
        
        [1]


- negative numbers
- duplicates?
- empty?

    aptr, bptr, cptr
    
    while loop:
        min(aptr, bptr, cptr)
        check arrays with min value -> move their pointer forward
    check for duplicates: compare last no in the result with the current min number
    
    
    TC: O(n+m+r)  SC: O(1)

"""

def merge_arrays(arr1, arr2, arr3):
    aptr, bptr, cptr = 0, 0, 0
    result = []
    
    while aptr < len(arr1) or bptr < len(arr2) or cptr < len(arr3): # 1, 2, 0
        num1 = arr1[aptr] if aptr < len(arr1) else float('inf') # 4
        num2 = arr2[bptr] if bptr < len(arr2) else float('inf') # 4
        num3 = arr3[cptr] if cptr < len(arr3) else float('inf') # 3
        
        min_val = min(num1, num2, num3) # 2
        if not result or result and result[-1] != min_val:
            result.append(min_val) # 1 2
            
        if min_val == num1:
            aptr += 1
        if min_val == num2:
            bptr += 1
        if min_val == num3:
            cptr += 1
            
    return result










"""
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "3+2*2"
Output: 7

Example 3:

Input: s = " 3+5 / 2 "
Output: 5

    - empty string -> 0


    - * and // 
    - O(n) O(n)
    
    3+2*2
         ^
    
    curr_num = 0
    curr_operator = +
    
    
    prev_num
    result: updated when we see + or -, update with digits before that operator (+-), add prev_num to result
    
    for ch in s:
        if ch is a digit:
            update the digit
        if ch is not digit and ch is an operator:
            if ch is + or -:
              result += prev_num if + or -prev_num
            if ch == * or /:
                prev_num * curr_num
    
    result += prev_num
    return result

"""

" 3£#£+3-3"
"333*222"


def evaluate_expression(s): # 3+2 * 2
    stack = []
    curr_num, curr_op = 0, '+'
    
    if not s[0].isdigit(): # curr_num=0, curr_op=*
        curr_op = s[0]
        
    for idx, ch in enumerate(s): # 2
        if ch.isdigit:
            curr_num = curr_num * 10 + int(ch) # 2
            
        if ch in '+-*/' or idx == len(s) - 1:
            if curr_op == '+':
                stack.append(curr_num)
            elif curr_op == '-':
                stack.append(-curr_num)
            elif curr_op == '*':
                stack.append(curr_num * stack.pop())
            elif curr_op == '/':
                stack.append(stack.pop() // curr_num)
            curr_num = 0
            curr_op = ch
                
    result = 0        # stack: 3 4
    while stack:
        result += stack.pop() # 3+4 = 7
        
    return result






















