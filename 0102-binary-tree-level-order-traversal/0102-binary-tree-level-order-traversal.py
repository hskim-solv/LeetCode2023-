# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        self.dfs(root, 0)
        return self.res
    
    def dfs(self, root, level):
        if level == len(self.res):
            self.res.append([])
        self.res[level].append(root.val)
        if root.left: self.dfs(root.left,level+1)
        if root.right: self.dfs(root.right,level+1)
        
        