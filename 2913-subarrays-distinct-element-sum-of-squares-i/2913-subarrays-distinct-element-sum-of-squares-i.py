class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        while nums:
            for s in range(1, len(nums)+1):
                ans += len(set(nums[:s]))**2
                ans += len(set(nums[s:]))**2
            if len(nums) > 1:
                nums.pop(0)
                nums.pop()
            else:
                break
        return ans