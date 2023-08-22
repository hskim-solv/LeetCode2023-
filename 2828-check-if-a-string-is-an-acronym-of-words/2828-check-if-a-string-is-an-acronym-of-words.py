class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return "".join(list(zip(*words))[0]) == s