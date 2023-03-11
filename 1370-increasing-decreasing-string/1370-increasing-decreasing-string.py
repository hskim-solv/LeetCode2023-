class Solution:
    def sortString(self, s: str) -> str:
        res = ""
        s = sorted(s)
        ss = sorted((set(s)))
        while s:
            for ch in ss:
                if ch in s:
                    res += ch
                    del s[s.index(ch)]
            for i in ss:
                if i not in s:
                    ss.remove(i)
            s = s[::-1]
            ss = ss[::-1]

                    
            

        return res     