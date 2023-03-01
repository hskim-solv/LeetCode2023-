class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        return [abs(sum(nums[:i])-sum(nums[1+i:])) for i in range(len(nums))]
