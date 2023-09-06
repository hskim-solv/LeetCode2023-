class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
            m = len(mat)
            n = len(mat[0])
            answer = [[sum(sum(mat[r][max(0,j-k):min(n,j+k+1)]) for r in range(max(0,i-k),min(m,i+k+1))) for j in range(n)] for i in range(m)]
            return answer