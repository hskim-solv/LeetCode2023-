class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = []
        while nums:
            n = nums.pop()
            if -n in nums:
                nums.remove(-n)
                res.append(abs(n))
        return max(res, default = -1)