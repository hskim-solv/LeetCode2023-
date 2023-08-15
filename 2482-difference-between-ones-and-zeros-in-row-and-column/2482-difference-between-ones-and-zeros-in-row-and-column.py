class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        cz = []
        m = len(grid)
        n = len(grid[0])

        for col in zip(*grid):
            cz.append(col.count(0))
        res = []
        for i in range(m):
            row = [n+m-2*grid[i].count(0)]*n


            for j in range(n):
                row[j]-=2*cz[j]
            res.append(row)
        return res
        