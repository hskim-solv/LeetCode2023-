class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = ans = len(nums)
        for s in range(2, len(nums)+1):
            for i in range(len(nums)+1-s):
                #print(nums[i:i+s],len(set(nums[i:i+s]))**2)
                ans += len(set(nums[i:i+s]))**2
        return ans