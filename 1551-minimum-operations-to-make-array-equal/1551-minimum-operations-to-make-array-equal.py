class Solution:
    def minOperations(self, n: int) -> int:
        return (n//2)*ceil(n/2)