class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        res = 0
        for key,v in Counter(s).items():
            if v < k:
                return max(*[ self.longestSubstring(ss,k) for ss in s.split(key)])
            else:
                res += v
        return res