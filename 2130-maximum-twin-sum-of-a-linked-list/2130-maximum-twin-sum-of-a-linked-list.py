# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        n = len(stack)
        mx = 0
        for l,r in zip(stack[:n//2],stack[n//2:][::-1]):
            sm = l+r
            if mx < sm:
                mx = sm
        return mx