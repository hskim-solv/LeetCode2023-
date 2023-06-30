class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = len(haystack.split(needle)[0])
        if res == len(haystack):
            return -1
        return res