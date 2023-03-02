class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return sum(i != j for i, j in zip_longest( bin(start)[:1:-1], bin(goal)[:1:-1],fillvalue='0' ))
