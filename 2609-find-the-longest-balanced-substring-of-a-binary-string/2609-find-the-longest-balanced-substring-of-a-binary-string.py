class Solution:
    def __init__(self):
        self.d = []
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        if len(set(s))==1:
            return 0
        length = len(s)
        cnt = 0
        l = []
        tmp = []
        for k,g in groupby(s):
            lg = list(g)
            cnt += len(lg)
            tmp += lg
            if k == '1':
                l.append("".join(tmp))
                tmp = []
            if cnt >= length:
                break
        if len(l) > 1:
            return max(map(self.findTheLongestBalancedSubstring,l))
        else:
            if s[0] == '0'and s[-1] == '1' and s.count('1') == s.count('0'):
                return length
            if s in self.d:
                return 0
            self.d.append(s)
            return max(
                        self.findTheLongestBalancedSubstring(s[1:]),
                       self.findTheLongestBalancedSubstring(s[:-1]) 
            )
        