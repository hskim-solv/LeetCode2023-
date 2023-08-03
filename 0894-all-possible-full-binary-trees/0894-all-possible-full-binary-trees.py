# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cache = defaultdict(list)
        self.cache[1].append(TreeNode())
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n in self.cache:
            return self.cache[n]
        for i in range(n, -1, -2):
            self.cache[n] += [ TreeNode(left=l,right=r) for r in self.allPossibleFBT(n - i - 1) for l in self.allPossibleFBT(i) ]
        return self.cache[n]