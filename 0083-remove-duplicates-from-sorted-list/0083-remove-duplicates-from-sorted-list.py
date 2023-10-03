# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode],order=0) -> Optional[ListNode]:
        if head and head.next:
            head.next = self.deleteDuplicates(head.next,order+1)
            return head.next if head.val == head.next.val else head
        return head