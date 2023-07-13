class Solution:
    def __init__(self):
        self.d = []
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        if s in self.d:
            return 0
        else:
            self.d.append(s)
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
                print(l,s)
                break
        if len(l) > 1:
            return max(self.findTheLongestBalancedSubstring(ss) for ss in l)
        if length % 2 == 0:
            if length//2 == s[length//2:].count('1') == s[:length//2].count('0'):
                return length
        return max(
                    self.findTheLongestBalancedSubstring(s[1:]),
                   self.findTheLongestBalancedSubstring(s[:-1]) 
                    )