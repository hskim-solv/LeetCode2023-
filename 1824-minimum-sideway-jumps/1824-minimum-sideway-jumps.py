class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [1, 0, 1]
        for stone in obstacles:
            if stone:
                dp[stone - 1] = inf
            for i in range(3):
                if stone != i + 1:
                    dp[i] = min(dp[i], dp[(i + 1) % 3] + 1, dp[(i + 2) % 3] + 1)
        return min(dp)