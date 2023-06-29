class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = list(columnTitle)
        res = 0
        lvl = 0
        while columnTitle:
            res += (ord(columnTitle.pop())-64)*(26**lvl)
            lvl += 1
        return res