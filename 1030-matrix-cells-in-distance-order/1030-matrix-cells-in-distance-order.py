class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        d = {}
        for i in range(rows):
            for j in range(cols):
                d[(i,j)] = abs(rCenter-i) + abs(cCenter-j)
        res = list(d.keys())
        res.sort(key=lambda x:d[x])
        return res
        #print(dir(res.sort))