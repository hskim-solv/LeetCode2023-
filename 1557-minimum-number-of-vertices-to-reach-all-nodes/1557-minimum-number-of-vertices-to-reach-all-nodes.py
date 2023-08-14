class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        p = list(zip(*edges))
        
        
        return set(p[0])-set(p[1])
        