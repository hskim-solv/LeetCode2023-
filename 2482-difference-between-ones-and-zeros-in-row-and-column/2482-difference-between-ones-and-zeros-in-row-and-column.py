class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rz = []
        cz = []
        m = len(grid)
        n = len(grid[0])
        for row in grid:
            rz.append(row.count(0))
        for col in zip(*grid):
            cz.append(col.count(0))
        res = []
        for i in range(m):
            row = []
            _rz = rz[i]
            _ro = n-_rz
            for j in range(n):
                _cz = cz[j]
                _co = m-_cz
                row.append(_ro+_co-_rz-_cz)
            res.append(row)
        return res
        