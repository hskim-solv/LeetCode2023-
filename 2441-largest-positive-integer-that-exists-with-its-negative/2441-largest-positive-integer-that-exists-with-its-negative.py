class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for n in nums:
            if n < 0 and -n in nums:
                return -n
        return -1