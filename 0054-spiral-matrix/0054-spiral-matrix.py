class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res =[]
        col = deque(zip(*matrix))
        row = deque(matrix)
        res += row.popleft()
        res += col.pop()[1:]
        i = 2
        while row or col:
            div,mod = divmod(i,4)
            if row:
                if mod == 0:
                    #print('000',row[0],mod,div,res)
                    res += row.popleft()[div:-1-div]
                    #print(res)
                elif mod == 2:
                 
                    #print('222',row[-1],mod,div,res)
                    res += reversed(row.pop()[div:-1-div])
                    #print(res)
            if col:
                if mod == 1:
                    res += col.pop()[div:-div]

                elif mod == 3:
                    #print('333',col[0],mod,div,res)
                    res += reversed(col.popleft()[1+div:-1-div])
                    #print(res)

            i += 1

        return res