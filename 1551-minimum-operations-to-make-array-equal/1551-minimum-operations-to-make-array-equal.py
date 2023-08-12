class Solution:
    def minOperations(self, n: int) -> int:
        return floor(n/2)*ceil(n/2)