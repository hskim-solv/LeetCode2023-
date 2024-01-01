class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid),len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    ans += 2
                    if i == 0:
                        ans += grid[i][j]
                    if j == 0:
                        ans += grid[i][j]
                if i == n-1:
                    ans += grid[i][j]
                else:
                    ans += abs(grid[i][j]-grid[i+1][j])
                if j == m-1:
                    ans += grid[i][j]
                else:
                    ans += abs(grid[i][j]-grid[i][j+1])

        return ans