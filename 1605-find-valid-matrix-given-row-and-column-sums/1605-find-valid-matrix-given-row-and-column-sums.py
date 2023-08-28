class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = [ [0]*len(colSum) for _ in range(len(rowSum)) ]
       
        
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                m[i][j] = min(rowSum[i],colSum[j])
                rowSum[i] -= m[i][j]
                colSum[j] -= m[i][j]
        return m