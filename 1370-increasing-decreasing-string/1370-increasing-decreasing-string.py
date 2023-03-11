class Solution:
    def sortString(self, s: str) -> str:
        res = ""
        s = sorted(s)
        ss = sorted((set(s)))
        while any(s):
            for ch in ss:
                if ch and ch in s:
                    res += ch
                    s[s.index(ch)] = None
                    if ch not in s:
                        ss[ss.index(ch)] = None
                        
            s = s[::-1]
            ss = ss[::-1]

        return res     