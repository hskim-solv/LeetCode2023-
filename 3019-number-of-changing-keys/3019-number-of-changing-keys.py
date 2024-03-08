class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        return sum(ch1 != ch2 for ch1, ch2 in zip(s[:-1],s[1:]))