class Solution:
    def sumScores(self, s: str) -> int:
        score = 0
        for k in range(1,len(s)):
            if s[-k]!=s[0]:
                continue
            if s[-k:]==s[:k]:
                score += k
                continue
            for i in range(k):

                if s[-k+i] != s[i]:
                    score += i
                    break

        return score+len(s)