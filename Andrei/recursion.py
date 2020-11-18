def getFact(num):
    fact = 1
    while num > 0:
        fact *=num
        num-=1

    return fact

print(getFact(2))


def getFactR(num):
    if num == 1:
        return 1

    return (num) * getFactR(num-1)

print(getFactR(5))

#  0,1,1,2,3,5,8,13,21,34

def fibo(index):
    if index == 0:
        return 0
    pos =  1
    fib = [0,1]
    while pos != index:
        fib.append(fib[pos]+fib[pos-1])
        pos+=1
    return fib[index]

print(fibo(10))

def fiboR(index):
    if index < 2:
        return index
    
    return fiboR(index-1) + fiboR(index-2)

print(fiboR(10))

# function reverseStringRecursive (str) {
#   if (str === "") {
#     return "";
#   } else {
#     return reverseStringRecursive(str.substr(1)) + str.charAt(0);
#   }
# }

def reversestring(string):
    if string == "":
        return ""
    return reversestring(string[1:]) + string[0]

print(reversestring("olumide"))
     

# Don't use zero as base case

# fib_cache - {}

# optimal solution using memoization
# def fiboR(index):
#     if index in fib_cache:
#         return fib_cache[index]
#     if index < 2:
#         return index
    
#     value = fiboR(index-1) + fiboR(index-2)
#     fib_cache[index] = value
#     return value


# Recursion Examples
# Merge sort, Quick Sort
# Tree Traversal
# Graph Traversal



# Bootle necks
# Stack Overflow
# Space Complexity

# Pros
# Readability
# sometimes efficiency especially with memoization
