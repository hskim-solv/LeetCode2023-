class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        for i in range(len(words)):
            words[i] = words[i].split(separator)
        return filter(lambda x: x,chain(*words))