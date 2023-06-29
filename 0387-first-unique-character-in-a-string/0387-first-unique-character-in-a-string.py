class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        for i, ss in enumerate(s):
            if 1 == d[ss]:
                return i
        return -1