class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        points.sort()
        return max( [ p1[0] - p0[0] for p0, p1 in zip( points[:-1], points[1:] ) ] )
            