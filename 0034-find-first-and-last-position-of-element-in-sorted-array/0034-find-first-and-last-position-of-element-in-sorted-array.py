class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def helper(nums,target,base):
            length = len(nums)
            if length == 0:
                return [-1,-1]
            mid = len(nums) // 2
            if target < nums[mid]:
                return helper(nums[:mid],target,base)
            elif target > nums[mid]:
                return helper(nums[mid+1:],target,base+mid+1)
            else:
                idx = nums.index(nums[mid])
                cnt = nums.count(nums[mid])-1
                return [base+idx,base+idx+cnt]
        return helper(nums,target,0)
