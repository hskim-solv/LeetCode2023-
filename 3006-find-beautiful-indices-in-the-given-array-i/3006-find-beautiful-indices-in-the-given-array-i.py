class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        ans = []
        sa = s[:]
        len_a = len(a)
        len_b = len(b)
        ia = 0
        ib = 0
        acc = 0
        while a in sa and b in s:
            idx1 = sa.index(a)
            idx2 = s.index(b)
            #print(abs((ia+idx1)-(ib+idx2) ))
            if abs((ia+idx1)-(ib+idx2) ) <= k:
                sa = sa[idx1+len_a:] 
                #print(sa)
                ans.append(ia+idx1)
                ia += idx1+len_a
                
            elif (ia+idx1)-(ib+idx2) > k :
                s = s[idx2+len_b:]
                ib += idx2+len_b
            elif (ib+idx2)-(ia+idx1) > k :
                sa = sa[idx1+len_a:]  
                ia += idx1+len_a
            #print(idx1,idx2,ia,ib,sa,s)
        return ans