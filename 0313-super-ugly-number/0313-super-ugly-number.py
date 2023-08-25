class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        size = len(primes)
        dp, idx, ugly_nums = [1], [0] * size, [1] * size
        for i in range(1, n):
            while dp[-1] in ugly_nums:
                j = ugly_nums.index(dp[-1])
                #print(dp, idx, ugly_nums,idx[j])
                ugly_nums[j] = dp[idx[j]] * primes[j]
                idx[j] += 1
            dp.append(min(ugly_nums))
            rest = min(idx)
            if min(idx) > 0:
                del dp[:rest]
                for i in range(size):
                    idx[i] -= rest
        return dp[-1]
        
            