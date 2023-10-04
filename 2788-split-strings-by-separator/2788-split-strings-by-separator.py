class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        for i in range(len(words)):
            words[i] = filter(lambda x: x,words[i].split(separator))
        return chain(*words)