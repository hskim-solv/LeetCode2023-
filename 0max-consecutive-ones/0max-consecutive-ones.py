class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0
        while 0 in nums:
            mx = max(mx,sum(nums[:nums.index(0)]))
            del nums[:nums.index(0)+1]
        mx = max(mx, sum(nums))
        return mx
            