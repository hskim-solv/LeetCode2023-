class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans, n = 0, len(nums)
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if not i * j % k and nums[i] == nums[j]:
                    ans += 1
        return ans
                    