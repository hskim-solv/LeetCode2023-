class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        res = set()
        for x, y in zip(sorted(s1), sorted(s2)):
            if ord(x) == ord(y):
                continue
            res.add(ord(x) >= ord(y))
            if len(res) == 2:
                return False
                
        return True