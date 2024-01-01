class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]):
            return mat
        ans = []
        mat = list(chain(*mat))

        for i in range(0, r*c, c):
            ans.append(mat[i:i+c])
        return ans