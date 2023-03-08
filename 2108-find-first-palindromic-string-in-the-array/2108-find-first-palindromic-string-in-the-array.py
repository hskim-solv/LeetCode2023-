class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        words = deque(words)
        while words:
            word = words.popleft()
            if word == word[::-1]:
                return word
        return ""