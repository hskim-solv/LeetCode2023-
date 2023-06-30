class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = haystack.split(needle)[0]
        if res == haystack:
            return -1
        return len(res)