class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n & 1:
            return n << 1
        return n