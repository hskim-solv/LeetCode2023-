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
        res = []
        self.dfs(root, 0, res)
        return res
    
    def dfs(self, root, level, res):
        if level == len(res):
            res.append([])
        res[level].append(root.val)
        if root.left: self.dfs(root.left,level+1,res)
        if root.right: self.dfs(root.right,level+1,res)
        
        