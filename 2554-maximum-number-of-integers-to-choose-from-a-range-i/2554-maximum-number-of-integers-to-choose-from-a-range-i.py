class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        total = 0
        cnt = 0
        for i in range(1, min(n,maxSum)+1):
            if i not in banned:
                if maxSum-total >= i:
                    total += i
                    cnt += 1
                if total >= maxSum:
                    break
    
        return cnt