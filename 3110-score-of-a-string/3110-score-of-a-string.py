class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(map(lambda x: abs(ord(x[0])-ord(x[1])), pairwise(s)))
        #return sum(abs(ord(x)-ord(y)) for x, y in pairwise(s))
            