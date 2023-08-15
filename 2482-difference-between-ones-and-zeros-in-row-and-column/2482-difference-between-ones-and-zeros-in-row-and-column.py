class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        cz = []
        m = len(grid)
        n = len(grid[0])

        for col in zip(*grid):
            cz.append(col.count(0))
        res = []
        for i in range(m):
            _rz = grid[i].count(0)

            res.append([n+m-2*(cz[j]+_rz) for j in range(n)])
        return res
        