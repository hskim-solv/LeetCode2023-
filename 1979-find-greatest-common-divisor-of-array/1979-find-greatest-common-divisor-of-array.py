class Solution:
    def findGCD(self, nums: List[int]) -> int:
        #nums.sort()
        return gcd(max(nums),min(nums))