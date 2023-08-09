class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return sum( map(  max, grid + list( zip(*grid) ) ) ) + sum(sum(e>0 for e in row) for row in grid ) 
        