class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for m in range(len(mat)-1):
            for n in range(len(mat[0])-1):
                for i in range(min(n+1,m+1)):
                    if mat[m-i][n-i] > mat[m+1-i][n+1-i]:
                        mat[m-i][n-i], mat[m+1-i][n+1-i] =  mat[m+1-i][n+1-i], mat[m-i][n-i]
        return mat
            