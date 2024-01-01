class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    res += 4
                    if i+1 != n and grid[i+1][j]:
                        res -= 2
                    if j+1 != m and grid[i][j+1]:
                        res -= 2
        return res