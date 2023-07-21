class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s): return 0
        if k == 1: return len(s)
        res = 0
        length = len(s)
        while res < length:
            for key,v in Counter(s).items():
                if v < k:
                    return max(self.longestSubstring(ss,k) if len(ss) else 0 for ss in s.split(key) )
                res += v
        return res