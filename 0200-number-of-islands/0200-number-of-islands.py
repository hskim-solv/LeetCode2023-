class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        def convert(i,j):
            if 0 < i and grid[i-1][j] == "1":
                grid[i-1][j] = "*"
                convert(i-1,j)
            if m-1>i and grid[i+1][j] == "1":
                grid[i+1][j] = "*"
                convert(i+1,j)
            if 0<j and grid[i][j-1] == "1":
                grid[i][j-1] = "*"
                convert(i,j-1)
            if n-1>j and grid[i][j+1] == "1":
                grid[i][j+1] = "*"
                convert(i,j+1)
            return 
        
        for i in range(m):
            row = grid[i]
            for j in range(n):
                if row[j] == "1":
                    row[j] = "*"
                    convert(i,j)
                    cnt += 1
        return cnt
    