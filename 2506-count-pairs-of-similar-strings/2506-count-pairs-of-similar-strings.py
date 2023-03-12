class Solution:
    def similarPairs(self, words: List[str]) -> int:
        cnt = 0
        for i in range(len(words)-1):
            wi = set(words[i])
            for j in range(i+1, len(words)):
                if wi == set(words[j]):
                    cnt += 1
        return cnt
                