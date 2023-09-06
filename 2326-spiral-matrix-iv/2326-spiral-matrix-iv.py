# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        res = [[0 for _ in range(n)] for _ in range(m)]
        
        left = 0
        down = 0
        while True:
            #print(left, n ,down, m)
            for j in range(left,n):
                #print('fr',res)
                if head:
                    res[down][j] = head.val
                    head = head.next
                else:
                    res[down][j] -= 1
            down += 1
            if down == m:
                return res

            for i in range(down, m):
                #print('du',res)
                if head:
                    res[i][n-1] = head.val
                    head = head.next
                else:
                    res[i][n-1] -= 1
                #print(res[i][-1-right])
            
            n -= 1
            if left == n:
                return res
            
            for j in range(n-1, left-1, -1):
                #print('rf',res,n-1,left-1)
                if head:
                    res[m-1][j] = head.val
                    head = head.next
                else:
                    res[m-1][j] -= 1
                    

            m -= 1
            if down == m:
                return res
            
            for i in range(m-1,down-1,-1):
                #print('ud',res,i,n)
                if head:
                    res[i][left] += head.val
                    head = head.next
                else:
                    res[i][left] -= 1
                #print('ud',res,i,m)
            left += 1
            if left == n:
                return res

        return res