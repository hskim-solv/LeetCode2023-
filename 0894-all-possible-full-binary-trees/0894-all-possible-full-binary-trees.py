# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
    if n == 1:
      return [TreeNode()]
    if n == 3:
      return [TreeNode(left=TreeNode(),right=TreeNode())]
    ret = []
    for i in range(1, n, 2):
      for left in self.allPossibleFBT(i):
        for right in self.allPossibleFBT(n - i - 1):
          
          ret.append(
            
            TreeNode(
          left=left,
          right=right
          )
          
          )
    return ret