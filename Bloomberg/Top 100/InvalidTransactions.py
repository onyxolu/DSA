# input = ["alice,20,800,mtv","alice,50,100,beijing"]

# We need to find a way to keep track of transactions with the same name

import collections


def invalidTransactions(self, transactions):
    if not transactions:
        return []
    # Hashmap to store , multiple values in a key as a list of tuples
    memo = collections.defaultdict(list)
    invalid = set()  # set of tuples to avoid repeated invalid trans. Id for uniqueness

    for i, transaction in enumerate(transactions):
        name, time, money, city = transaction.split(
            ",")  # save each transaction in an array
        time, money = int(time), int(money)
        # first check
        if money > 1000:
            invalid.add((transaction, i))
        # second check
        for prev_time, prev_city, prev_i, prev_trans in memo[name]:
            if abs(time - prev_time) <= 60 and city != prev_city:
                invalid.add((transaction, i))
                invalid.add((prev_trans, prev_i))

        memo[name].append((time, city, i, transaction))

    # Return array with all the first values in tuple
    return [trans for trans, _ in invalid]


print(invalidTransactions(
    ["alice,20,800,mtv", "alice,20,800,mtv", "alice,50,100,beijing"]))
