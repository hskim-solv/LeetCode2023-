class Solution:
    def sumScores(self, s: str) -> int:
        score = 0
        for k in range(1,len(s)):
            if s[-k]!=s[0]:
                continue
            if s[-k:]==s[:k]:
                score += k
                continue
            for c1,c2 in zip(s[-k:],s[:k]):
                if c1!=c2:
                    break
                score += 1
        return score+len(s)