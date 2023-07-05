class Solution:
    def __init__(self):
        self.d = {}
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1 or m == 1:
            return 1
        if n > m:
            m, n = n, m
        if (m, n) not in self.d:
            self.d[(m, n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return self.d[(m, n)]