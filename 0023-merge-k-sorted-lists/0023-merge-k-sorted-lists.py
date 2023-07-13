# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        l = []
        Node = ListNode(val=0,next=None)
        head = Node
        for i in range(k):
            if lists[i]:
                l.append(lists[i].val)
            else:
                l.append(inf)
        while any(lists):
            idx = l.index(min(l))
            if lists[idx]:
                if lists[idx].next:
                    l[idx] = lists[idx].next.val
                else:
                    l[idx] = inf
            Node.next = lists[idx]
            lists[idx] = lists[idx].next
            Node = Node.next
        return head.next
        