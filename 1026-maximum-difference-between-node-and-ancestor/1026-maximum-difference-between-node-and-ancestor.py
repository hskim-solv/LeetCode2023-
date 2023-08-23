# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def Diff(root,mn,mx):
            return max(Diff(root.left,min(root.val,mn),max(root.val,mx) ),Diff(root.right,min(root.val,mn),max(root.val,mx) )) if root else mx - mn
        return Diff(root,root.val,root.val)