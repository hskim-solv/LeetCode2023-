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
                    res += row.popleft()[div:-1-div]
                elif mod == 2:
                    res += reversed(row.pop()[div:-1-div])
            if col:
                if mod == 1:
                    res += col.pop()[div:-div]
                elif mod == 3:
                    res += reversed(col.popleft()[1+div:-1-div])
            i += 1

        return res