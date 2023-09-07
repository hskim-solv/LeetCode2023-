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
        l, r = [], []
        half = len(grid)//2
        for row in grid:
            stack.update(row)
            l.append(row[:half])
            r.append(row[half:])
            if len(stack) > 1:
                
                for i in range(len(l),half*2):
                    l.append(grid[i][:half])
                    r.append(grid[i][half:])
                    
                return Node(val=1, 
                            isLeaf=0,
                           topLeft=self.construct(l[:half]),
                           topRight=self.construct(r[:half]),
                           bottomLeft=self.construct(l[half:]),
                           bottomRight=self.construct(r[half:]),
                           )
        return Node(val=grid[0][0], isLeaf=1)

        
        