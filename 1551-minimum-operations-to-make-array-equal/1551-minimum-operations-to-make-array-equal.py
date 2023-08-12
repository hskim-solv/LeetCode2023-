class Solution:
    def minOperations(self, n: int) -> int:
        return sum( n//2 for n in range(1,n+1) )