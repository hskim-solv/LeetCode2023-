# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        stack = deque([root])
        while stack:
            if not root.left and root.right:
                return False
            root = stack.popleft()
            if root.left:
                stack.append(root.left)
            if not root.right and stack and stack[0].left:
                return False
            
            if root.right:
                stack.append(root.right)
        return True