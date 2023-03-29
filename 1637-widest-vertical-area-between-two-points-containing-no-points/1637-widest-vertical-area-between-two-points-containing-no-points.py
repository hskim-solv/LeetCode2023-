class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        max_width = 0
        prev_x = points[0][0]
        prev_y = points[0][1]
        now_y = 0
        for x,y in sorted(points):
            if max_width < x - prev_x:

                max_width = x - prev_x
            prev_x = x

        return max_width
            