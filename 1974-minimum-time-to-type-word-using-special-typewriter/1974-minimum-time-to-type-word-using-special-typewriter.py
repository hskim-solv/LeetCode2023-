class Solution:
    def minTimeToType(self, word: str) -> int:
        p = 97
        sec = 0
        for s in word:
            diff = abs(ord(s) - p)
            p = ord(s)
            sec += 1
            if diff > 13:
                sec += (26-diff)
            else:
                sec += diff
        return sec