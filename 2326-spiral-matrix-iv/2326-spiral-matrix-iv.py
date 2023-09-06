# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        res = [[0 for _ in range(n)] for _ in range(m)]
        
        lrdu = [0, n-1, 0, m-1]
        while True:
            for x, y, z in ((0, 1, 2),(2, 3, 1),(1, 0, 3),(3, 2, 0)):
                if x > y:
                    rng = range(lrdu[x], lrdu[y]-1, -1)
                else:
                    rng = range(lrdu[x], lrdu[y]+1)
                if x in (0, 1):
                    for i in rng:
                        if head:
                            res[lrdu[z]][i] = head.val
                            head = head.next
                        else:
                            res[lrdu[z]][i] = -1
                elif x in (2, 3):
                    for i in rng:
                        if head:
                            res[i][lrdu[z]] = head.val
                            head = head.next
                        else:
                            res[i][lrdu[z]] = -1

                if z in (0,2):
                    lrdu[z] += 1
                else:
                    lrdu[z] -= 1 
                #print(lrdu)
                if (lrdu[2] > lrdu[3]) or (lrdu[0] > lrdu[1]):
                    return res
                

        return res