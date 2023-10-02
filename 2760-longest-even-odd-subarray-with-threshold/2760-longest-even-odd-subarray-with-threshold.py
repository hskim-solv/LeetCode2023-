class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        mx = 0
        for l in range(len(nums)):
            if nums[l] % 2 or nums[l] > threshold: 
                continue
            for r in range(l+1, len(nums)):
                if nums[r] > threshold or nums[r-1] % 2 == nums[r] % 2: 
                    break
                mx = max(mx, r+1-l)
            if mx == 0:
                mx = 1
        return mx