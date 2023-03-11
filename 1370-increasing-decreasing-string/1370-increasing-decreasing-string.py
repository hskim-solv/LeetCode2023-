class Solution:
    def sortString(self, s: str) -> str:
        res = ""
        s = list(s)
        s.sort()
        ss = list(set(s))
        ss.sort()
        while s:
            for ch in ss[:]:
                if ch in s:
                    res += ch
                    s.remove(ch)
                else:
                    ss.remove(ch)
            
            s.reverse()
            ss.reverse()

                    
            

        return res     