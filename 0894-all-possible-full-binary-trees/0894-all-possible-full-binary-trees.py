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

          
          ret.append(
            
            TreeNode(
          left=self.clone(left) if right_count < len(right_branch) else left,
          right=self.clone(right) if left_count < len(left_branch) else right
          )
          
          )
    return ret