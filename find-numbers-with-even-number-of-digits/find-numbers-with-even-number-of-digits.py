class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum( not len(str(n)) & 1 for n in nums)