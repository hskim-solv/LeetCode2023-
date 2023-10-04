class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return chain(*[filter(lambda x: x, word.split(separator)) for word in words])