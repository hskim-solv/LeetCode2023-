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
    if n == 3:
      return [TreeNode(left=TreeNode(),right=TreeNode())]
    ret = []
    for i in range(1, n, 2):
      for left_count, left in enumerate(self.allPossibleFBT(i), 1):
        for right_count, right in enumerate(self.allPossibleFBT(n - i - 1), 1):

          
          ret.append(
            
            TreeNode(
          left=self.clone(left),
          right=self.clone(right)
          )
          
          )
    return ret