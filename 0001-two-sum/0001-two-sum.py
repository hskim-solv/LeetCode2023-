class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums)-1
        sorted_nums = sorted(nums)
        while l < r:
            s = sorted_nums[l] + sorted_nums[r]
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                res = [nums.index(sorted_nums[l])]
                nums[res[0]] = None
                return res+[nums.index(sorted_nums[r])]