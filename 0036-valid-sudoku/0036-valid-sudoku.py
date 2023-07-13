class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digits = {'1','2','3','4','5','6','7','8','9'}
        for row in board:
            if self.isRowCul(row):
                return False
        for cul in zip(*board):
            if self.isRowCul(cul):
                return False
        for n in [0,3,6]:
            for m in [0,3,6]:
                if self.isRowCul(board[n+0][m+0:m+3]+board[n+1][m+0:m+3]+board[n+2][m+0:m+3]):
                    return False
        return True
    def isRowCul(self,rowcul: List[str]) -> bool:
        for k,v in Counter(rowcul).items():
            if k.isdigit():
                if v != 1:
                    return True
        return False
        
            
        
        
    #def isRow(self, row: List[str]) -> bool:
        
    #def isColSudoku(self,cul: List[str]) -> bool:
        
    #def isSquareSudoku(self,sqr: List[List[str]]) -> bool:
        
        
        