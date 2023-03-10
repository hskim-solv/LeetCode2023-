class Solution:
    def generateTheString(self, n: int) -> str:
        return 'ba'[n & 1] + "a" * (n - 1) 
