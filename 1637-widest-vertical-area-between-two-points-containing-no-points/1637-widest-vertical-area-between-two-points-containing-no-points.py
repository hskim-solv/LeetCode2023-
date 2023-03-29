class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        max_width = 0
        prev_x = points[0][0]

        for x, _ in sorted(points):
            if max_width < x - prev_x:
                max_width = x - prev_x
            prev_x = x

        return max_width
            