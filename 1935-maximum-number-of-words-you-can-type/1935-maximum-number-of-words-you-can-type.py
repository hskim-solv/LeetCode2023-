class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(" ")
        cnt = 0
        brokenLetters = set(brokenLetters)
        for word in text:
            #flag = True
            word = set(word)
            if len(word) == len(word-brokenLetters):
                cnt += 1

        return cnt
            