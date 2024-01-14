class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        ans = []
        sa = s[:]
        len_a = len(a)
        len_b = len(b)
        ia = 0
        ib = 0
        while a in sa and b in s:
            idx1 = sa.index(a)
            idx2 = s.index(b)
            x = ia+idx1-ib-idx2
            if x > k:
                s = s[idx2+len_b:]
                ib += idx2+len_b
            elif -x > k:
                sa = sa[idx1+len_a:]  
                ia += idx1+len_a
            else:
                sa = sa[idx1+len_a:] 
                ans.append(ia+idx1)
                ia += idx1+len_a
        return ans