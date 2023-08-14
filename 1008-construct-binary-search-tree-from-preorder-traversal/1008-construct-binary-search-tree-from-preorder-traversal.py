# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(val=preorder.pop(0))
        
        for v in preorder:
            self.bst(root,v)
        return root
    
    def bst(self, root, val):
        if root.val > val:
            if root.left: 
                self.bst(root.left,val)
            else:
                root.left = TreeNode(val=val)
        else:
            if root.right:
                self.bst(root.right,val)
            else:
                root.right = TreeNode(val=val)