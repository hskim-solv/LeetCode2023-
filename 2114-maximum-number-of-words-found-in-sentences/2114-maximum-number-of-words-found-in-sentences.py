class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum = 0
        while sentences:
            diff = sentences.pop().count(" ") - maximum
            if diff > 0:
                maximum += diff 
        return maximum + 1
        