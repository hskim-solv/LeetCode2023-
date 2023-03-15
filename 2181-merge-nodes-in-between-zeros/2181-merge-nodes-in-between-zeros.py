# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        s = 0
        while head.next:
            if head.next.val:
                s += head.next.val
                head.next = head.next.next
            else:
                head.val = s
                s = 0
                if head.next.next:
                    head = head.next
                else:
                    head.next = None
        return root
                