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
                jumps = nums[i:i+j]
                for s in range(1, len(jumps)):
                    jumps[s] += s
                i += jumps.index(max(jumps))
            else:
                return cnt
            
        return cnt