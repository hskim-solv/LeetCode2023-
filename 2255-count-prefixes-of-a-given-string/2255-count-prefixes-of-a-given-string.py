class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        cnt = 0
        while words:
            cnt += s.startswith(words.pop())
        return cnt
        