class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i = 0
        cnt = 0
        n = len(nums)
        if nums[i] >= n-1:
            return 1
        while i < n-1:
            j = nums[i]
            cnt += 1
            if i+j < n-1:
                i += 1
                jumps = nums[i:i+j]
                for s in range(1, len(jumps)):
                    jumps[s] += s
                i += jumps.index(max(jumps))
            else:
                return cnt
            
        return cnt