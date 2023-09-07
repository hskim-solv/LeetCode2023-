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
        for i in range(len(grid)):
            stack.update(grid[i])
            if len(stack) > 1:
                half = len(grid)//2
                colgrid=list(zip(*grid))
                l = list(zip(*colgrid[:half]))
                r = list(zip(*colgrid[half:]))

                return Node(val=1, 
                            isLeaf=0,
                           topLeft=self.construct(l[:half]),
                           topRight=self.construct(r[:half]),
                           bottomLeft=self.construct(l[half:]),
                           bottomRight=self.construct(r[half:]),
                           )
        return Node(val=grid[0][0], isLeaf=1)

        
        