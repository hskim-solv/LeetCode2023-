# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for _ in range(n)] for _ in range(m)]
        druf = [0, n-1, m-1, 0]
        def rnge(x, y):
            if x > y:
                return range(x, y-1, -1)
            return range(x, y+1)
        def rowcol(x, z, i, head):
            if x in (1, 3):
                res[z][i] = head.val
                return head.next
            else:
                res[i][z] = head.val
                return head.next
        while head:
            for x, y, z in ((3, 1, 0),(0, 2, 1),(1, 3, 2),(2, 0, 3)):
                for i in rnge(druf[x], druf[y]):
                    if head:
                        head = rowcol(x,druf[z],i,head)
                    else:
                        return res
                if z in (0,3):
                    druf[z] += 1
                else:
                    druf[z] -= 1 
        return res