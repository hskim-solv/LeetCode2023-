class Solution:
    def __init__(self):
        self.d=[]
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        if s in self.d:
            return 0
        length = len(s)
        if length == 1:
            return 0
        l, r = set(s[:length//2]), set(s[length//2:])

        if len(l) ==1 and len(r)==1:
            if '1' not in l and '0' not in r:
                if length % 2 == 0:
                    return length
        self.d.append(s)
        return max(
            
            self.findTheLongestBalancedSubstring(s[1:]),
                   self.findTheLongestBalancedSubstring(s[:-1])
            
        )
        