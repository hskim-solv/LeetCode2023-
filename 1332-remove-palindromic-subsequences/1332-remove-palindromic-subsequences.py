class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return (s != s[::-1]) + 1 