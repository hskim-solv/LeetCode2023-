class Solution:
    def partitionString(self, s: str) -> int:
        i = 0
        cnt = 1
        for j in range(len(s)):
            if s[j] in s[i:j]:
                cnt += 1
                i = j
        return cnt