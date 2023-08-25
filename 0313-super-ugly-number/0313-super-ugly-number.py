class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        size = len(primes)
        dp, idx = [1], [0] * size
        
        for _ in range(n-1):
            m = inf
            for j in range(size):
                m = min(m,dp[idx[j]] * primes[j])
            for j in range(size):
                if m==dp[idx[j]] * primes[j]:
                    idx[j] += 1
            #print(dp,idx,m)
            dp.append(m)
            rest = min(idx)
            if  rest > 0:
                del dp[:rest]
                for i in range(size):
                    idx[i] -= rest
        return dp[-1]
        
            