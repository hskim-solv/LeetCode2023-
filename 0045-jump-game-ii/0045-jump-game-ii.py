class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)-1
        if n == 0: return 0  
        j = nums[0]
        i = 0
        cnt = 1
        while i+j < n:
            cnt += 1
            i += 1
            jumps = [order+jump for order,jump in enumerate(nums[i:i+j], 1)]
            i += jumps.index(max(jumps))
            j = nums[i]
        return cnt
