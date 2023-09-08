class Solution:
    def __init__(self):
        self.cache = defaultdict(int)
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1: return len(word2)
        if not word2: return len(word1)

        if (word1, word2) not in self.cache:
            self.cache[(word1, word2)] = min(
                            self.minDistance(word1[:-1], word2[:-1])+1,
                            self.minDistance(word1, word2[:-1])+1,
                            self.minDistance(word1[:-1], word2)+1, 
                            
                        )
        if word1[-1] == word2[-1]:
            return self.minDistance(word1[:-1], word2[:-1])
        return self.cache[(word1,word2)]