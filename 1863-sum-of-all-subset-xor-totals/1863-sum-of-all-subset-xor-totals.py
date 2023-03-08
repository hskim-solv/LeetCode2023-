class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = sum(nums)
        for i in range(2, len(nums) + 1):
            for j in combinations(nums,i):
                ans += reduce(lambda x, y: x ^ y ,j ) 
        return ans
        