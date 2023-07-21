class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res, length = 0, len(s)
        while res < length:
            for key,v in Counter(s).items():
                if v < k:
                    return max(self.longestSubstring(ss,k) if k <= len(ss) else 0 for ss in s.split(key) )
                res += v
        return res