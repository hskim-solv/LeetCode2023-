class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] > threshold or nums[0] % 2 == 1 else 1
        ln = len(nums)
        mx = 0
        for l in range(ln):
            if nums[l] % 2 == 1:
                continue
            if nums[l] > threshold:
                continue
            for r in range(l+1, ln):
                if nums[r] > threshold:
                    break
                if nums[r-1] % 2 == nums[r] % 2:
                    break
                mx = max(mx, r+1-l)
                print(r,l)
            if mx == 0:
                mx = 1
        return mx