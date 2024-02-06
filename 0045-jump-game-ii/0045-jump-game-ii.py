class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)-1
        if n == 0: return 0  
        i = 0
        cnt = 1
        while i+nums[i] < n:
            cnt += 1
            i += 1
            jumps = [i+j for i, j in enumerate(nums[i:i+nums[i-1]], 1)]
            i += jumps.index(max(jumps))
        return cnt
