'''

Given a list of positive values, we are asked to randomly pick up a value based on the weight of each value. To put it simple, the task is to do sampling with weight.

Let us look at a simple example. Given an input list of values [1, 9], when we pick up a number out of it, the chance is that 9 times out of 10 we should pick the number 9 as the answer.

In other words, the probability that a number got picked is proportional to the value of the number, with regards to the total sum of all numbers.

To understand the problem better, let us imagine that there is a line in the space, we then project each number into the line according to its value, i.e. a large number would occupy a broader range on the line compared to a small number. For example, the range for the number 9 should be exactly nine times as the range for the number 1.

Now, let us throw a ball randomly onto the line, then it is safe to say there is a good chance that the ball will fall into the range occupied by the number 9. In fact, if we repeat this experiment for a large number of times, then statistically speaking, 9 out of 10 times the ball will fall into the range for the number 9.

Voila. That is the intuition behind this problem.


EXPLANATION OF THE QUESTION CONCEPT, LEETCODE DIDN'T DO A GOOD JOB EXPLAINING THIS


Alternate example to understand the solution:

So lets relate this problem with a problem of dividing a cake in a party such that the person with highest weight has better chance to pick a slice.(proportional to his weight)

Suppose we have people with weight 1, 3, 5, 7, 9 pounds and they went for a party to a bakery and purchased a cake. They decided that lets add our total weight and buy a cake proportional to it. So their totalWeight came as
1+3+5+7+9 = 25
They purchased a 25 pound cake :).
They decided that lets cut cake in 1 pound slices(25 slices total) and whoever wants to eat can take a 1 pound slice at a time. The person who will pick a slice will be picked randomly.

To find out how to pick randomly and to figure out who will pick first, they first did a cumulative sum of their weights

1->1
3-> 1 + 3 = 4
5-> 4 + 5 = 9
7-> 7 + 9 = 16
9-> 9 + 16 = 25

=1,4,9,16,25

so the server is asked to pick a random number out of 25 for them. The random number represents a slice.
So it can be 17 out of 25 or 6 out of 25.

So the slice 1 belongs to 1 pounds person. Which is only 1 slice.
Slice between 2-4 belong to 3 pounds person. Which are 3 slices.
.
.
Slice between 17- 25 belong to the 9 pounds person. Which are 9 slices.

If we pick a random slice out of 25, there is a higher probability that it will belong to a person with 9 slices (the person with 9 pounds) , the person who own 7 slices has second highest probability. The person whose weight is 1 pound and has only 1 slice has least probability to pick a slice.

And that's what we wanted. We want to let the person with highest weight get a greater chance to pick a slice every time even though they are picked at random.

The question can also be asked in reverse.


In Statistics, if we nomalize (divided by self.cdf[-1]) the self.cdf into [0, 1], it's actually a discrete distribution cdf sequence. For cdf function, given X you can get the Cumulative Probability (aka percentile) of X, which is Prob(x <= X).

The question is actually asking to generate random samples given by a specific statistical distribution. How?

Principle is easy, take uniform sample from the cdf squence ( which can be realized by random ), then use inverse_cdf function to find the variable X. The binary search here is actually inverse_cdf function, that returns the X given by a Cumulative Probability.

After you take enough samples by this way, and plot the histogram of these samples, you will found the plot fits well for the given distribution.

More information and proof can be found in Wikipedia & StackExchange.

'''


'''

Sample input: 1,3
    cumulativ add - [1,4]

    so we use bst to find the random number, we can use linear search but bst is faster.
    So to generate a random weight, we generate random number between 0 - 1 and multiply with the maximum prefix, so whatever we generate is within range.

    So we need to find he index close to the number we generated, which is where BST comes in.



'''

# Prefix sum then we can do linear search
# But then linear search is 0(N)
# We can do better, we can use binary search 0(LogN)


class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum
        

    def pickIndex(self) -> int:
        random_num = self.total_sum * random.random() # random will give you a value from 0 to 1
        low,high = 0, len(self.prefix_sum)
        while low < high:
            mid = low + (high - low) // 2
            if random_num > self.prefix_sum[mid]:
                low = mid + 1
            else:
                high = mid
        return low