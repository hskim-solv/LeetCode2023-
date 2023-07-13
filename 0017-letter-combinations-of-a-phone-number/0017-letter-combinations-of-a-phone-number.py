class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res = []
        digits = list(digits)[::-1]
        while digits:
            if not res:
                res += d[digits.pop()]
            else:
                tmp = d[digits.pop()]
                res *= len(tmp)
                res.sort()
                for i in range(len(res)):
                    res[i] += tmp[i%len(tmp)]
        return res