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
      for left in self.allPossibleFBT(i):
        if i <= 3:
          l = left
        else:
          l = self.clone(left)
        for right in self.allPossibleFBT(n - i - 1):
          if n - i - 1 <= 3:
            r = right
          else:
            r = self.clone(right)

          
          ret.append(
            
            TreeNode(
          left=l,
          right=r
          )
          
          )
    return ret