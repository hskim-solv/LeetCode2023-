class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        res=[]
        for i,n in enumerate(nums):
            res.append(len(set(nums[:i+1]))-len(set(nums[i+1:])))
        return [len(set(nums[:i+1]))-len(set(nums[i+1:])) for i,n in enumerate(nums)]