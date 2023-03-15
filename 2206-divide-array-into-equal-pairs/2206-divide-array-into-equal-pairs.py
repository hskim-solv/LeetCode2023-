class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return not any(x & 1 for x in Counter(nums).values())  
      