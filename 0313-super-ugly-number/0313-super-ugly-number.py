class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly, dp, idx, ugly_nums = 1, [1], [0] * len(primes), [1] * len(primes)
        for i in range(1, n):
            while ugly in ugly_nums:
                j = ugly_nums.index(ugly)
                ugly_nums[j] = dp[idx[j]] * primes[j]
                idx[j] += 1
            # get the minimum
            ugly = min(ugly_nums)
            dp.append(ugly)
        return dp[-1]
        
            