class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        res = []
        if len(original) == m*n:
            original.reverse()
            for j in range(m):
                row = []
                for i in range(n):
                        row.append(original.pop())
                res.append(row)

        return res