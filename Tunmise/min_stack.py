class MinStack:

    def __init__(self):
        self.stack_values = []
        self.stack_minima = []

    def push(self, x: int) -> None:
        self.stack_values.append(x)
        current_min = self.stack_minima[-1] if self.stack_minima else math.inf
        if x <= current_min: # `<=` instead of `<` because a duplicate of the minimum can now be pushed
            self.stack_minima.append(x)

    def pop(self) -> None:
        if self.stack_values.pop() == self.stack_minima[-1]:
            self.stack_minima.pop()

    def top(self) -> int:
        return self.stack_values[-1]

    def getMin(self) -> int:
        return self.stack_minima[-1]