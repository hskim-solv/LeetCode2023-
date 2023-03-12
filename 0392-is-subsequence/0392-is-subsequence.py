class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        for i in s:
            l += 1
            if i in t:
                l -= 1 
                t = t[t.index(i)+1:]
        return l == 0
       
