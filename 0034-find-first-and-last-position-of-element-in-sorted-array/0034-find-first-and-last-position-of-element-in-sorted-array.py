class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.helper(nums,target,0)
    
    def helper(self, nums: List[int], target: int, base: int) -> List[int]:
        if not nums:
            return [-1,-1]
        mid = len(nums) // 2
        if not mid:
            if nums[0]==target:
                return [base,base]
            return [-1,-1]

        if target < nums[mid]:
            return self.helper(nums[:mid],target,base)
        elif target > nums[mid]:
            return self.helper(nums[mid+1:],target,base+mid+1)
        else:
            idx = nums.index(nums[mid])
            cnt = nums.count(nums[mid])-1
            return [base+idx,base+idx+cnt]