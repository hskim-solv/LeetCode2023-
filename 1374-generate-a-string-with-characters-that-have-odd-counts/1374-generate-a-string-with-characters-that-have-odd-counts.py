class Solution:
    def generateTheString(self, n: int) -> str:
        return "a" * (n-1) + ('a' if n & 1 else 'b')
