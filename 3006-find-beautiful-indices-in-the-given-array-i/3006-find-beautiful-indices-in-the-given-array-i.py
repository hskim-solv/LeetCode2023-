class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        ans = []
        sa = s[:]


        while a in sa and b in s:
            idx1 = sa.index(a)
            idx2 = s.index(b)
            if abs(idx1-idx2) <= k:
                ans.append(idx1)
                sa = sa[:idx1] + '*'*len(a) + sa[idx1+len(a):]  
            elif idx1-idx2 > k :
                s = s[:idx2] + '*'*len(b) + s[idx2+len(b):]
            elif idx2-idx1 > k :
                sa = sa[:idx1] + '*'*len(a) + sa[idx1+len(a):]  
        return ans