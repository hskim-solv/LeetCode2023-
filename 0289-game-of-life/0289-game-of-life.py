class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            row = [i]
            box = board[i][:]
            for j in range(n):
                cul = [j]
                if i > 0:
                    row.append(i-1)
                if j > 0:
                    cul.append(j-1)
                if i < m-1:
                    row.append(i+1)
                if j < n-1:
                    cul.append(j+1)
                nv = list(set(product(row,cul)))
                nv.remove((i,j))
                nnv = sum([board[ii][jj] for ii,jj in nv])
                if box[j]:
                    if nnv not in [2,3]:
                        box[j]=0  
                else:
                    if nnv == 3:
                        box[j]=1
            if i > 0:
                board[i-1] = pre_box
            pre_box = box[:]
        board[-1] = pre_box


