class BrowserHistory:

    def __init__(self, homepage: str):
        self.url_list = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        self.pos += 1 
        self.url_list = self.url_list[:self.pos] + [url]
        #self.url_list.append(url)

    def back(self, steps: int) -> str:
        self.pos = max(0, self.pos-steps)
        return self.url_list[self.pos]

    def forward(self, steps: int) -> str:
        self.pos = min(self.pos+steps, len(self.url_list)-1)
        return self.url_list[self.pos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)