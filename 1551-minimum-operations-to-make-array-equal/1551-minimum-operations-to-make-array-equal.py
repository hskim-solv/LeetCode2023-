class Solution:
    def __init__(self):
        self.cache = defaultdict(int)
        self.cache[1] = 0
        self.cache[2] = 1
    def minOperations(self, n: int) -> int:
        if n not in self.cache:
            self.cache[n] = n//2 + self.minOperations(n-1)
        return self.cache[n]