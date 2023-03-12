class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):return False
        if len(s) == 0:return True

        l = len(s)
        for i in s:
            while t := deque(t):
                if i == t.popleft():
                    l -= 1
                    break 
        return not l
       
