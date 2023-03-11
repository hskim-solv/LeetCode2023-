class Solution:
    def sortString(self, s: str) -> str:
        res = ""
        s = list(s)
        ss = sorted(set(s))
        rr = ss.copy()
        rr.reverse()
        while s:
            for sr in (ss,rr):
                for ch in sr:
                    if ch in s:
                        res += ch
                        s.remove(ch)
                s.reverse()
        return res    