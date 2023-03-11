class Solution:
    def sortString(self, s: str) -> str:
        res = ""
        is_asc = True
        s = list(s)
        while s:
            box = ""
            is_asc = not is_asc
            s.sort(reverse = is_asc)
            for ch in s[:]:
                #print(res,box,ch,s)
                if box == ch:
                    continue
                else:
                    res += ch
                    box = ch
                    s.remove(ch)
                    
            

        return res     