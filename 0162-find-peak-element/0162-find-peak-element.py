class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        middle = len(nums)//2
        def find(nums):
            if len(nums)<3:
                return max(nums)
            middle = len(nums)//2
            return max(find(nums[:middle]),find(nums[middle:]))
        return nums.index(find(nums))