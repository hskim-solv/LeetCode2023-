class Solution:
    def repeatedCharacter(self, s: str) -> str:
        for i in range(len(s)):
            l = []
            for letter in s:
                if letter in l:
                    return letter
                l.append(letter)