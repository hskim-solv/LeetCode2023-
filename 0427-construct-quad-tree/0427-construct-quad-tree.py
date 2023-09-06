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
        # 그리드가 전부 같은 값인지 판별
        if len(grid) == 1:
            return Node(val=grid[0][0], isLeaf=1)
        stack = []
        for row in grid:
            stack = list(set(stack+row))
            if len(stack) != 1:
                n = len(grid)
                half = n//2
                return Node(val=1, 
                            isLeaf=0,
                           topLeft=self.construct([grid[i][:half] for i in range(half)]),
                           topRight=self.construct([grid[i][half:] for i in range(half)]),
                           bottomLeft=self.construct([grid[i][:half] for i in range(half, n)]),
                           bottomRight=self.construct([grid[i][half:] for i in range(half, n)]),
                           )
        return Node(val=stack[0], isLeaf=1)

        
        