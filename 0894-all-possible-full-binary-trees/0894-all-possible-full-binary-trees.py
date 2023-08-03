# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def clone(self, tree: TreeNode) -> TreeNode:
    if not tree:
      return None
    return TreeNode(left=self.clone(tree.left),right=self.clone(tree.right))
  
  def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
    if n == 1:
      return [TreeNode()]
    ret = []
    for i in range(1, n, 2):
      left_branch = self.allPossibleFBT(i)
      right_branch = self.allPossibleFBT(n - i - 1)
      for left_count, left in enumerate(left_branch, 1):
        for right_count, right in enumerate(right_branch, 1):
          tree = TreeNode()
          
          # If we're using the last right branch, then this will be the last time this left branch is used and can hence
          # be shallow copied, otherwise the tree will have to be cloned
          tree.left = self.clone(left) if right_count < len(right_branch) else left
          
          # If we're using the last left branch, then this will be the last time this right branch is used and can hence
          # be shallow copied, otherwise the tree will have to be cloned
          tree.right = self.clone(right) if left_count < len(left_branch) else right
          
          ret.append(tree)
    return ret