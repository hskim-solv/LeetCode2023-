class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum = 0
        while sentences:
            maximum = max(sentences.pop().count(" "), maximum)
        return maximum + 1
        