class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        self.pos += 1 
        self.urls = self.urls[:self.pos]
        self.urls.append(url)

    def back(self, steps: int) -> str:
        self.pos = max(0, self.pos-steps)
        return self.urls[self.pos]

    def forward(self, steps: int) -> str:
        self.pos = min(self.pos+steps, len(self.urls)-1)
        return self.urls[self.pos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)