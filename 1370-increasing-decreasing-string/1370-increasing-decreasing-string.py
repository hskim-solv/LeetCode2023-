class Solution:
    def sortString(self, s: str) -> str:
        res = ""
        s = sorted(s)
        ss = sorted((set(s)))
        while s:
            for ch in ss[:]:
                if ch in s:
                    res += ch
                    del s[s.index(ch)]
                    if ch not in s:
                        del ss[ss.index(ch)]
                        

            s = s[::-1]
            ss = ss[::-1]

                    
            

        return res     