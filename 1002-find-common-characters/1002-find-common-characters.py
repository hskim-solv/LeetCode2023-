class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        return list(reduce(collections.Counter.__and__, map(collections.Counter, words)).elements())