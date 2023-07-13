"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = defaultdict(lambda : Node(0))
        d[None] = None
        n = head
        while n:
            d[n].val = n.val
            d[n].next = d[n.next]
            d[n].random = d[n.random]
            n = n.next
        return d[head]