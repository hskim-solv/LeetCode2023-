class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        d = {}
        for i in range(rows):
            for j in range(cols):
                d[(i,j)] = abs(rCenter-i) + abs(cCenter-j)

        return sorted(d.keys(),key=lambda x:d[x])
        