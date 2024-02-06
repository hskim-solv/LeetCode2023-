# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def helper(node, low, high):
            if not node: 
                return high - low
            return min(
                helper(node.left, low, node.val), 
                       helper(node.right, node.val, high)
            )
        return helper(root, float('-inf'), float('inf'))