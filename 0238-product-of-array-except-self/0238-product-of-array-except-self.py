class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        z_count = nums.count(0)
        if not z_count:
            total = reduce(lambda x, y: x * y, nums, 1)
            return [total//nums[i] for i in range(len(nums))]
        elif z_count == 1:
            i = nums.index(0)
            res = [0] * len(nums)
            res[i] = reduce(lambda x, y: x * y, nums[:i]+nums[i+1:], 1)
            return res
        else:
            return [0] * len(nums)