class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]):
            return mat
        if r == len(mat) and c == len(mat[0]):
            return mat

        mat = [i for row in mat for i in row]

        return [mat[i:i+c] for i in range(0, r*c, c)]