class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.reverse()
        while nums:
            n = nums.pop()
            print(nums,abs(n+k),nums.count(abs(n-k)),ans)
            ans += nums.count(n+k)
            ans += nums.count(n-k)
        return ans