class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [sum(row) for row in mat]
        cols = [sum(col) for col in zip(*mat)]
        ans = 0
        n, m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if rows[i] == 1 and cols[j] == 1:
                        ans += 1

        return ans