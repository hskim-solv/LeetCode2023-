class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i,j)
                    break
            if start:
                break
        self.res = []
        def step(i, j, grid):
            if grid[i][j] == -1:
                return
            elif grid[i][j] == 2:
                for row in grid:
                    if 0 in row:
                        return
                self.res.append(1)
            elif grid[i][j] == 0:
                grid[i][j] = -1
                if i > 0:
                    step(i-1, j, deepcopy(grid))
                if i < m-1:
                    step(i+1, j, deepcopy(grid))
                if j > 0:
                    step(i, j-1, deepcopy(grid))
                if j < n-1:
                    step(i, j+1, deepcopy(grid))
        grid[start[0]][start[1]] = 0
        step(start[0],start[1], grid)
        return sum(self.res)
        