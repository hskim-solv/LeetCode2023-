class Solution:
    def sortString(self, s: str) -> str:
        res = ""
        s = sorted(s)
        ss = sorted(set(s))

        while s:
            for st in (ss,ss[::-1]):
                for ch in st:
                    if ch in s:
                        res += ch
                        s.remove(ch)
                s.reverse()

        return res    