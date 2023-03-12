class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
         return sum([ 1 for w in words[left:right+1] if w[0] in ('a','e','i','o','u') and w[-1] in ('a','e','i','o','u') ])