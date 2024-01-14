class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        ans = []
        sa = s[:]
        len_a = len(a)
        len_b = len(b)
        aglue = '*'*len_a
        bglue = '*'*len_b
        while a in sa and b in s:
            idx1 = sa.index(a)
            idx2 = s.index(b)
            if abs(idx1-idx2) <= k:
                ans.append(idx1)
                sa = sa[:idx1] + aglue + sa[idx1+len_a:] 
            elif idx1-idx2 > k :
                s = s[:idx2] + bglue + s[idx2+len_b:]
            elif idx2-idx1 > k :
                sa = sa[:idx1] + aglue + sa[idx1+len_a:]  
        return ans