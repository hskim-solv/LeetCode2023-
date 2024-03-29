class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))

        length = len(nums)
        res = 0
        i = 0
        j = 1
        while j < length:
            if nums[j] - nums[i] == j - i:
                res = max(res,j - i)
                j += 1
            else:
                i = j
                j = i+1
        return res+1
        