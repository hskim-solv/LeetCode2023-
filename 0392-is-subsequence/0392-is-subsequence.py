class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = len(s)
        for i in s:
            while t := deque(t):
                if i == t.popleft():
                    l -= 1
                    break 
        return not l
       
