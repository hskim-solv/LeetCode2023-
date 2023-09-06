class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
            m = len(mat)
            n = len(mat[0])
            answer = []
            for i in range(m):
                row = []
                for j in range(n):
                    box = sum(sum(mat[r][max(0,j-k):min(n,j+k+1)]) for r in range(max(0,i-k),min(m,i+k+1)))

                    row.append(box)
                answer.append(row)
            return answer