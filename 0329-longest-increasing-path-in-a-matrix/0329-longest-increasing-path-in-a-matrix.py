class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.d = defaultdict(int)
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        res = 0
        for m in range(self.m):
            for n in range(self.n):
                if (m,n) not in self.d:
                    self.d[(m,n)] = self.search(matrix,m,n,1)
                res = max(res,self.d[(m,n)])
        return res
        
    def search(self,matrix,i,j,res):
        point = matrix[i][j]    
        new_res =res
        if self.m-1 > i and matrix[i+1][j] > point: #up
            if (i+1,j) not in self.d:
                self.d[(i+1,j)] = self.search(matrix,i+1,j,1)
            new_res = max(new_res,(self.d[(i+1,j)]+res))
        if 0 < i and matrix[i-1][j] > point: #down
            if (i-1,j) not in self.d:
                self.d[(i-1,j)] = self.search(matrix,i-1,j,1)
            new_res = max(new_res,(self.d[(i-1,j)]+res))
        if 0 < j and matrix[i][j-1] > point: #left
            if (i,j-1) not in self.d:
                self.d[(i,j-1)] = self.search(matrix,i,j-1,1)
            new_res = max(new_res,(self.d[(i,j-1)]+res))
        if self.n-1 > j and matrix[i][j+1] > point: #right
            if (i,j+1) not in self.d:
                self.d[(i,j+1)] = self.search(matrix,i,j+1,1)
            new_res = max(new_res,(self.d[(i,j+1)]+res))
        return new_res