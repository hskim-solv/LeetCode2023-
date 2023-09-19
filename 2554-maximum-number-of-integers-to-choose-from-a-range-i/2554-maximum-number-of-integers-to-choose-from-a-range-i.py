class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        top = min(n,maxSum)
        banned = sorted(set(banned))
        if banned[0] > top:
            banned = []
        while banned and banned[-1] > top:
            banned.pop()
        total = 0
        cnt = 0
        for i in range(1, top+1):
            if i not in banned:
                if maxSum-total >= i:
                    total += i
                    cnt += 1
                if total >= maxSum:
                    break
            if banned and banned[0] < i:
                banned.pop(0)
            

        
        return cnt