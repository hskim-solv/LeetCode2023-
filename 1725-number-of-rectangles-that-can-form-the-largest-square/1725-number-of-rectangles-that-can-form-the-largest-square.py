class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        return (rectangles := list(map(min,rectangles))).count(max(rectangles))