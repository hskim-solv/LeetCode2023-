class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = len(nums)
        for s in range(2, len(nums)+1):
            for i in range(len(nums)+1-s):
                ans += len(set(nums[i:i+s]))**2
        return ans