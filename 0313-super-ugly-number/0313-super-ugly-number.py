class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        size = len(primes)
        ugly, dp, index, ugly_nums = 1, [1], [0] * size, [1] * size
        for i in range(1, n):
            # compute possibly ugly numbers and update index
            for j in range(0, size):
                if ugly_nums[j] == ugly:
                    ugly_nums[j] = dp[index[j]] * primes[j]
                    index[j] += 1
            if min(index) > 0:
                rest = min(index)
                del dp[:rest]
                for i in range(size):
                    index[i] -= rest 
            # get the minimum
            ugly = min(ugly_nums)
            dp.append(ugly)
        return dp[-1]
        
            