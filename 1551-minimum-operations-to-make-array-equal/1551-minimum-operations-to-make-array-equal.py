class Solution:
    def minOperations(self, n: int) -> int:
        return sum( i*2 for i in range(1,(n+1)//2) ) + (n//2 if not n % 2 else 0)