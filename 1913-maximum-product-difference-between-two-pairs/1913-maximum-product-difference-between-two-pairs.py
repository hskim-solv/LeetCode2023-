class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        return prod(heapq.nlargest(2, nums)) - prod(heapq.nsmallest(2, nums))
