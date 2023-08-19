class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if sum(colsum) != upper + lower:
            return []
        res = [[],[]]
        m = colsum.count(2)
        upper -= m
        lower -= m
        for n in colsum:
            if n == 2:
                res[0].append(1)
                res[1].append(1)
            elif n == 0:
                res[0].append(0)
                res[1].append(0)
            else:
                if upper > 0:
                    upper -= 1
                    res[0].append(1)
                    res[1].append(0)
                elif lower > 0:
                    lower -= 1
                    res[0].append(0)
                    res[1].append(1)
                else:
                    break

        if upper != 0 or lower != 0:
            return []

        return res