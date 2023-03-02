class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        return reduce(lambda x,y: x*y,heapq.nlargest(2, nums)) - reduce(lambda x,y: x*y,heapq.nsmallest(2, nums))