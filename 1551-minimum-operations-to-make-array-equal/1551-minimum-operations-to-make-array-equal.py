class Solution:
    def minOperations(self, n: int) -> int:
        return 2*sum( i for i in range(1,(n+1)//2) ) + (0 if n % 2 else n//2)