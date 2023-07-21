class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s: return 0
        if k == 1: return len(s)
        if k > 10**4: return 0
        
        res = 0
        for key,v in Counter(s).items():
            if v < k:
                return max(self.longestSubstring(ss,k) for ss in s.split(key))
            res += v
        return res