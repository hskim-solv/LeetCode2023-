class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        return self.findd(nums)
    
    def isd(self,nums):
        if len(nums)==1:
            return False
        if len(set(nums))!=len(nums):
            return True
        return False
    
    def findd(self,nums):
        l = len(nums)//2
        if self.isd(nums[:l]):
            return self.findd(nums[:l])
        elif self.isd(nums[l:]):
            return self.findd(nums[l:])
        else:
            return nums[l]