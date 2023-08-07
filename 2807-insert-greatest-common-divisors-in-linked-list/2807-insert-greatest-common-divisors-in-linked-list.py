# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        v1 = node.val
        while node.next:
            v2 = node.next.val
            node_next = node.next
            node.next = ListNode(val=gcd(v1,v2),next=node_next)
            v1 = v2
            node = node.next.next
        return head