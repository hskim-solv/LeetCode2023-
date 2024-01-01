class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        r, c = len(board), len(board[0])
        ans = 0
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'R':
                    for left in range(j-1, -1, -1):
                        if board[i][left] == 'B':
                            break
                        if board[i][left] == 'p':
                            ans += 1
                            break
                    for right in range(j+1, c):
                        if board[i][right] == 'B':
                            break
                        if board[i][right] == 'p':
                            ans += 1
                            break
                    for up in range(i-1, -1, -1):
                        if board[up][j] == 'B':
                            break
                        if board[up][j] == 'p':
                            ans += 1
                            break
                    for down in range(i+1, r):
                        if board[down][j] == 'B':
                            break
                        if board[down][j] == 'p':
                            ans += 1
                            break
        return ans
                        
                    