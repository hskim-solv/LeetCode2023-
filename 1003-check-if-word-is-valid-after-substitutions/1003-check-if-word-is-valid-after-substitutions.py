class Solution:
    def isValid(self, s: str) -> bool:
        while "abc" in s:
            s = "".join(s.split("abc"))
        return not s