class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        original.reverse()
        res = []
        for j in range(m):
            row = []
            for i in range(n):
                if original:
                    row.append(original.pop())
                else:
                    return []
            res.append(row)
        if original:
            return []
        return res