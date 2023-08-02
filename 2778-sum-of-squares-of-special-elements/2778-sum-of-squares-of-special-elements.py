class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            if not n % (i+1):
                res += nums[i]**2
        return res