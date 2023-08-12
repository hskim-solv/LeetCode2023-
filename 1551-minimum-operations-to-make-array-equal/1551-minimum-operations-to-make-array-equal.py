class Solution:
    def __init__(self):
        self.cache = {1:0}
    def minOperations(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        return n//2 + self.minOperations(n-1)