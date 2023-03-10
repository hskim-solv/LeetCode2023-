class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(pref == word[:len(pref)] for word in words)