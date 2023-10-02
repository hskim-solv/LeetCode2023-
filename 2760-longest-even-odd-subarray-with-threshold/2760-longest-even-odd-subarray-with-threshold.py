class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ln = len(nums)
        mx = 0
        for l in range(ln):
            if nums[l] % 2 == 1 or nums[l] > threshold: 
                continue

            for r in range(l+1, ln):
                if nums[r] > threshold or nums[r-1] % 2 == nums[r] % 2: 
                    break
                mx = max(mx, r+1-l)
                #print(r,l)
            if mx == 0:
                mx = 1
        return mx