class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = sorted( list(zip(*points) )[0] )
        return max( [ x1 - x0 for x0, x1 in zip( xs[:-1], xs[1:] ) ] )
            