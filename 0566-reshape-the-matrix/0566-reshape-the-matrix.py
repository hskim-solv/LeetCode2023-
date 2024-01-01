class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        if r*c != n*m:
            return mat
        if r == n and c == m:
            return mat

        mat = [i for row in mat for i in row]

        return [mat[i:i+c] for i in range(0, r*c, c)]