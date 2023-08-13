class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = m*n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    cnt -= 1
                elif grid[i][j] == 1:
                    x0,y0 = i,j
        m -= 1
        n -= 1
        res = [0]
        def dfs(path):
            x, y = path[-1]
            if grid[x][y] == -1:
                return
            if grid[x][y] == 2:
                if len(path)==cnt:
                    res[0] += 1
                else:
                    return
            
            if x != 0:
                if [x-1,y] not in path:
                    dfs(path + [ [x-1,y] ])
            if y != 0:
                if [x,y-1] not in path:
                    dfs(path + [ [x,y-1] ])
            if m != x:
                if [x+1,y] not in path:
                    dfs(path + [ [x+1,y] ])
            if n != y:
                if [x,y+1] not in path:
                    dfs(path + [ [x,y+1] ])
            
        
        dfs([[x0,y0]])

        return res[0]