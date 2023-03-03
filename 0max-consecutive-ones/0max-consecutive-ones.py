class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(sum(g) if k else 0 for k,g in groupby(nums))
            