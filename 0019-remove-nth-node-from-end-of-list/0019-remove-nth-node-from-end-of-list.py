# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return head.next
        stack = []
        
        while head:
            stack.append(head)
            head=head.next
        if n == len(stack):
            return stack[1]
        stack[-n-1].next = stack[-n].next

        return stack[0]