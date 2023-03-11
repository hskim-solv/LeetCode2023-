class Solution:
    def sortString(self, s: str) -> str:
        res = ""
        s = sorted(s)
        ss = sorted(set(s))
        rr = sorted(set(s), reverse=True)
        while s:
            for sr in (ss,rr):
                for ch in sr:
                    if ch in s:
                        res += ch
                        s.remove(ch)
       
                s.reverse()

        return res    