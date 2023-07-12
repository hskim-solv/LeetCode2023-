class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)//2
        print(nums)
        if self.isd(nums[:l]):
            return self.findDuplicate(nums[:l])
        elif self.isd(nums[l:]):
            return self.findDuplicate(nums[l:])
        else:
            return nums[l]
    def isd(self,nums):
        if len(nums)==1:
            return False
        if len(set(nums))!=len(nums):
            return True
        return False
    