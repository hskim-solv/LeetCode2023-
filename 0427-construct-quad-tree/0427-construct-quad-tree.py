"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        stack = set()
        for row in grid:
            stack.update(row)
            if len(stack) != 1:
                half = len(grid)//2
                return Node(val=1, 
                            isLeaf=0,
                           topLeft=self.construct([grid[i][:half] for i in range(half)]),
                           topRight=self.construct([grid[i][half:] for i in range(half)]),
                           bottomLeft=self.construct([grid[i][:half] for i in range(half, 2*half)]),
                           bottomRight=self.construct([grid[i][half:] for i in range(half, 2*half)]),
                           )
        return Node(val=grid[0][0], isLeaf=1)

        
        