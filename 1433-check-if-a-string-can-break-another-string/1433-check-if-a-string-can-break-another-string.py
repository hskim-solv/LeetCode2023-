class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        res1 = []
        res2 = []
        for x, y in zip(sorted(s1), sorted(s2)):
            res1.append(ord(x) >= ord(y))
            res2.append(ord(x) <= ord(y))
        return all(res1) or all(res2)