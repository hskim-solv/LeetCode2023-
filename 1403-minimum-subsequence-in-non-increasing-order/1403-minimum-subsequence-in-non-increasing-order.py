class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        mid = sum(nums)//2
        total = 0
        for i, n in enumerate(nums, 1):
            total += n
            if mid < total:
                return nums[:i]