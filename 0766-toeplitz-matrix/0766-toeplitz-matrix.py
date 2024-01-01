class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        if m == 1 or n == 1:
            return True
        for i in range(m-2,-1,-1):
            if len({matrix[i+step][step] for step in range(min(m-i, n))}) != 1:
                return False
        for j in range(n-2,0,-1):
            print(m,n,j)
            if len({matrix[step][j+step] for step in range(min(n-j, m))}) != 1:
                return False
        return True