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
            if i+j < n-1:
                jumps = nums[i+1:i+1+j]
                for s in range(len(jumps)):
                    jumps[s] += s
                i += 1
                i += jumps.index(max(jumps))
            else:
                return cnt+1
            cnt += 1
        return cnt