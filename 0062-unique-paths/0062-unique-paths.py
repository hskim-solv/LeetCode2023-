class Solution:
    @cache
    def uniquePaths(self, m: int, n: int) -> int:
        if n > m:
            m, n = n, m
        if n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)