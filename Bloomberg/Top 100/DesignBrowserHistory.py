class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.current += 1
        self.history = self.history[:self.current]  # keep track of current
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.current = max(self.current-steps, 0)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(self.current+steps, len(self.history)-1)
        return self.history[self.current]
