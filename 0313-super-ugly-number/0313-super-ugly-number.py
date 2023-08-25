class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        size = len(primes)
        dp, idx, ugly_nums = [1], [0] * size, [1] * size
        for i in range(n-1):
            #print(dp,idx,ugly_nums)
            while dp[-1] in ugly_nums:
                j = ugly_nums.index(dp[-1])
                ugly_nums[j] = dp[idx[j]] * primes[j]
                idx[j] += 1
            dp.append(min(ugly_nums))
            if i % 2:
                rest = min(idx)
                if  rest > 0:
                    del dp[:rest]
                    for i in range(size):
                        idx[i] -= rest
        return dp[-1]
        
            