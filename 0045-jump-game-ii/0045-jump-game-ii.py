class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)-1
        if n == 0:
            return 0  
        if nums[0] == n:
            return 1
        i = 0
        cnt = 0
        while i < n:
            j = nums[i]
            cnt += 1
            if i+j < n:
                i += 1
                jumps = [i+s for i,s in enumerate(nums[i:i+j], 1)]
                i += jumps.index(max(jumps))
            else:
                return cnt
