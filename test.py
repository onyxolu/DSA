
# import random

# def startGame():
#     scor


def func(tickets, p):
    return sum([min(tickets[i], tickets[p]) if i <= p else min(tickets[i], tickets[p] -1) for i in range(len(tickets))])


print(func([5,2,6,3,4,5], 2))