class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        return sum( int(v==2) for v in Counter(["".join(sorted(word)) for word in words]).values() )