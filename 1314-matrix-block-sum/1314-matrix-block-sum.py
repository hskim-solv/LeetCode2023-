class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
            return [[sum(sum(mat[r][max(0,j-k):min(len(mat[0]),j+k+1)]) for r in range(max(0,i-k),min(len(mat),i+k+1))) for j in range(len(mat[0]))] for i in range(len(mat))]
