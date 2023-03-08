class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        #return next((for word in deque(words) if word == word[::-1]),"")
        #words = deque(words)
        while (words := deque(words)):
            if (word:=words.popleft()) == word[::-1]:
                return word
        return ""
