# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        depth_val = {}
        def dfs(root, i):
            if i not in depth_val:
                depth_val[i] = 0 
            if root.left:
                dfs(root.left, i+1)
            if root.right:
                dfs(root.right, i+1)
            if root.left is None and root.right is None:
                depth_val[i] += root.val
                return 
        dfs(root,1)
        return depth_val[max(depth_val)]