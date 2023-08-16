class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        mid = len(nums)//2
        mx = 0
        for n1,n2 in zip(nums[:mid],nums[mid:][::-1]):
            if mx < n1+n2:
                mx = n1+n2
        return mx
        #return max([n1+n2 for n1,n2 in zip(nums[:mid],nums[mid:][::-1])])
            