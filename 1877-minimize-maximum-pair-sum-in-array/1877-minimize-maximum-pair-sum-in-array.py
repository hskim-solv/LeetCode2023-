class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        mid = len(nums)//2
        return max([n1+n2 for n1,n2 in zip(nums[:mid],nums[mid:][::-1])])
            