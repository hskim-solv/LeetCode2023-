class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        size = len(primes)
        dp, idx, ugly_nums = deque([1]), [0] * size, [1] * size
        for i in range(1, n):
            #print(dp, idx, ugly_nums)
            while dp[-1] in ugly_nums:
                j = ugly_nums.index(dp[-1])
                ugly_nums[j] = dp[idx[j]] * primes[j]
                idx[j] += 1
            dp.append(min(ugly_nums))
            rest = min(idx)
            if rest > 0:
                for _ in range(rest):
                    dp.popleft()
                for i in range(size):
                    idx[i] -= rest
        return dp[-1]
        
            