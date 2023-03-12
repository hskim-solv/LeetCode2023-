class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = len(s)
        for i in s:
                if i in t:
                    l -= 1 
                    t = t[t.index(i)+1:]
                    print(l)
        return not l
       
