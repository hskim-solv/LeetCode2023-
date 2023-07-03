class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 not in nums:
            total = reduce(lambda x, y: x * y, nums, 1)
            return [total//nums[i] for i in range(len(nums))]
        elif nums.count(0) == 1:
            i = nums.index(0)
            return [0] * i + [reduce(lambda x, y: x * y, nums[:i]+nums[i+1:], 1)] + [0] *(len(nums)-i-1)
        else:
            return [0] * len(nums)