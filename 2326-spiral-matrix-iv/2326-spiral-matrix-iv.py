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
        while True:
            for x, y in ((3, 1),(0, 2),(1, 3),(2, 0)):
                if druf[x] > druf[y]:
                    rng = range(druf[x], druf[y]-1, -1)
                else:
                    rng = range(druf[x], druf[y]+1)
                if x in (3, 1):
                    for i in rng:
                        if head:
                            res[druf[z]][i] = head.val
                            head = head.next
                        else:
                            break
                else:
                    
                    for i in rng:
                        if head:
                            res[i][druf[z]] = head.val
                            head = head.next
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