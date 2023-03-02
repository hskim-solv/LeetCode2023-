class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        while nums:
            n = nums.pop()
            ans += nums.count(n+k)
            if n > k:
                ans += nums.count(n-k)
        return ans