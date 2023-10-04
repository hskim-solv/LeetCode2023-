class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        transposed = list(zip(*matrix))
        res = []
        
        for row in matrix:
            rmin = min(row)
            j = row.index(rmin)
            if max(transposed[j]) == rmin:
                res.append(rmin)
        return res