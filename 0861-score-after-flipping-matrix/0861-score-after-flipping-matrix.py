class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        res = (1 << N - 1) * M
        for j in range(1, N):
            cur = sum(row[j] == row[0] for row in grid)
            res += max(cur, M - cur) * (1 << N - 1 - j)
        return res