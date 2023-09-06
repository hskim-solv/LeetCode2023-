# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for _ in range(n)] for _ in range(m)]
        z=0
        druf = [0, n-1, m-1, 0]
        def rnge(x,y):
            if x > y:
                return range(x, y-1, -1)
            return range(x, y+1)
        def rowcol(x,z,i,head):
            if x in (1, 3):
                res[z][i] = head.val
                return head.next
            else:
                res[i][z] = head.val
                return head.next
        while True:
            for x, y in ((3, 1),(0, 2),(1, 3),(2, 0)):
                for i in rnge(druf[x], druf[y]):
                    if head:
                        head = rowcol(x,druf[z],i,head)
                    else:
                        break
                if z in (0,3):
                    druf[z] += 1
                else:
                    druf[z] -= 1 
                z += 1
                z %= 4
                if (druf[0] > druf[2]) or (druf[3] > druf[1]):
                    return res
        return res