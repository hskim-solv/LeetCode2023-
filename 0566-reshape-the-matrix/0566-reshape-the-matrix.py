class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]):
            return mat

        mat = list(chain(*mat))

        return [mat[i:i+c] for i in range(0, r*c, c)]