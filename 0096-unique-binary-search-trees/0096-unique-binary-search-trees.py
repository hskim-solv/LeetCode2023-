class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n <= 1: return 1
        return sum(self.numTrees(i-1) * self.numTrees(n-i) for i in range(1, n+1))
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
        #return factorial(2*n) // (factorial(n)*factorial(n+1))
        #return int(prod((4*i+2) / (i+2) for i in range(n)))