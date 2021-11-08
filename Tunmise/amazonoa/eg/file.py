
def insertno():
    LA = [1, 3, 5, 7, 8]

    #add 2 extra space at the end
    extra = [0] * 2
    LA += extra
    
    print(LA)

    item = 10
    k = 3
    n = 5
    i = 0
    j = n

    n = n + 1

    while j >= k:
        LA[j+1] = LA[j]
        j = j-1

    LA[k] = item

    #remove 
    LA.pop()

    for i in range(len(LA)):
        print("LA " + str(i) + " is " + str(LA[i]))

    

print(insertno())