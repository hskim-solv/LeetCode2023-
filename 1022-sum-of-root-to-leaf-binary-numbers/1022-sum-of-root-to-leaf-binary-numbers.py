# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root,bits):
            bits += str(root.val)
            if not root.left and not root.right:
                self.res += int(bits,2)
            if root.left: dfs(root.left, bits)
            if root.right: dfs(root.right, bits)
        dfs(root,"")
        return self.res