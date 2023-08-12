class Solution:
    @cache
    def minOperations(self, n: int) -> int:
        if n == 1:
            return 0
        return n//2 + self.minOperations(n-1)