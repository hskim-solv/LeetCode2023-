class Solution:
    def numTrees(self, n: int) -> int:
        return factorial(2*n) // (factorial(n)*factorial(n+1))
        #return int(prod((4*i+2) / (i+2) for i in range(n)))