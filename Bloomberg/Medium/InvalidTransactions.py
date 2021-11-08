# input = ["alice,20,800,mtv","alice,50,100,beijing"]

# We need to find a way to keep track of transactions with the same name

import collections

def invalidTransactions( transactions):
    if not transactions:
        return []
    memo = collections.defaultdict(list) # Hashmap to store , multiple values in a key as a list of tuples
    invalid = set()  # set of tuples

    
    for i, transaction in enumerate(transactions):
        content = transaction.split(",")  # save each transaction in an array
        name = content[0]
        time = int(content[1])
        money = int(content[2])
        city = content[3]
        
        # first check
        if money > 1000:
            invalid.add((transaction, i))
        # second check
        for prev_time, prev_city, prev_i, prev_trans in memo[name]:
            if abs(time - prev_time) <= 60 and city != prev_city:
                invalid.add((transaction, i))
                invalid.add((prev_trans, prev_i))
        
        memo[name].append((time, city, i, transaction))

    return [trans for trans, _ in invalid]   # Return array with all the first values in tuple


print(invalidTransactions(["alice,20,800,mtv","alice,20,800,mtv","alice,50,100,beijing"]))
