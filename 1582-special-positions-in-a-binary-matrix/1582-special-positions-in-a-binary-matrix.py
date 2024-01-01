class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_index = [i for i, row in enumerate(mat) if sum(row) == 1 ]
        col_index = [j for j, col in enumerate(zip(*mat)) if sum(col) == 1]
        ans = 0
        for i in row_index:
            for j in col_index:
                if mat[i][j] == 1:
                    ans += 1

        return ans