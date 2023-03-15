class Solution:
    def repeatedCharacter(self, s: str) -> str:
        l = []
        for letter in s:
            if letter in l:
                return letter
            l.append(letter)