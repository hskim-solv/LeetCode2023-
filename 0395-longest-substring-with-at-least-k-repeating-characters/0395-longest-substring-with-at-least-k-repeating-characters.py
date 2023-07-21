class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res, length = 0, len(s)
        while res < length:
            for key,v in Counter(s).items():
                if v < k:
                    return max(0 if k > len(ss) else self.longestSubstring(ss,k) for ss in s.split(key) )
                res += v
        return res