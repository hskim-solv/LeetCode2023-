class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        while nums:
            #print(nums,ans)
            for s in range(1, len(nums)+1):
                ans += len(set(nums[:s]))**2
                ans += len(set(nums[s:]))**2
            nums = nums[1:-1]
        return ans