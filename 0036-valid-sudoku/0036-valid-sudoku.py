class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if self.isl(row):
                return False
        for cul in zip(*board):
            if self.isl(cul):
                return False
        for n in [0,3,6]:
            for m in [0,3,6]:
                if self.isl(board[n+0][m+0:m+3]+board[n+1][m+0:m+3]+board[n+2][m+0:m+3]):
                    return False
        return True
    def isl(self,l: List[str]) -> bool:
        for k,v in Counter(l).items():
            if k.isdigit():
                if v != 1:
                    return True
        return False
        
            
        
        
    #def isRow(self, row: List[str]) -> bool:
        
    #def isColSudoku(self,cul: List[str]) -> bool:
        
    #def isSquareSudoku(self,sqr: List[List[str]]) -> bool:
        
        
        