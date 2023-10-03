# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root, bits):
            bits *= 2
            bits += root.val
            if root.left == root.right:
                self.res += bits
            if root.left: dfs(root.left, bits)
            if root.right: dfs(root.right, bits)

        dfs(root, 0)
        return self.res