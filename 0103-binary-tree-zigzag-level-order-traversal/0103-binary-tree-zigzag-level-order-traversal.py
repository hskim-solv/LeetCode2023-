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
        level = 0
        res = []
        q = deque([root])
        while q:
            res.append(deque([]))
            if level % 2:
                for _ in range(len(q)):
                    node = q.pop()
                    res[level].appendleft(node.val)
                    if node.left: q.appendleft(node.left)
                    if node.right: q.appendleft(node.right)
            else:
                for _ in range(len(q)):
                    node = q.pop()
                    res[level].append(node.val)
                    if node.left: q.appendleft(node.left)
                    if node.right: q.appendleft(node.right)
            level += 1
        return res