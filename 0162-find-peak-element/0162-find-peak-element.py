class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def find(nums):
            middle = len(nums)//2
            if middle < 2:
                return max(nums)
            return max(find(nums[:middle]),find(nums[middle:]))
        return nums.index(find(nums))