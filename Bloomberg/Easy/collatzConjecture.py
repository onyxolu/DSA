from collections import deque

class collatz:
    def __init__(self):
        self.dict = {}

    def compute(self, num):
        queue = deque([num])
        steps = 0
        print(num, "num")
        while num > 1:
            if num in self.dict:
                return steps + self.dict[num]
            if num % 2 == 0:
                num /=2
            else: num = 3 * num + 1
            queue.append(num)
            steps += 1
            print(num, steps, "nawa o")

        cnt = 0
        while queue:
            cur = queue.pop()
            cnt += 1
            self.dict[cur] = cnt

        return steps


collatz1 = collatz()
print(collatz1.compute(5))

