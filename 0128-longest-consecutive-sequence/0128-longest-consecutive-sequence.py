class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        length = len(nums)
        i,j = 0,1
        res = 1
        while j < length:
            if nums[j] - nums[i] == j - i:
                res = max(res,1+j - i)
                j += 1
            else:
                i += 1
                j = i+1
        return res
        