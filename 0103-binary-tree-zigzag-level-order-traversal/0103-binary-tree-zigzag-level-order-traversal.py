# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        evenodd = True
        res = deque([])
        q = deque([root])
        while q:
            res.append(deque([]))
            evenodd = not evenodd
            for _ in range(len(q)):
                node = q.pop()
                if evenodd:
                    res[-1].appendleft(node.val)
                else:
                    res[-1].append(node.val)
                if node.left: q.appendleft(node.left)
                if node.right: q.appendleft(node.right)
        return res