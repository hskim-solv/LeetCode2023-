class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        cnt = 0
        for i in range(1, n+1):
            if i not in banned:
                if maxSum >= i:
                    maxSum -= i
                    cnt += 1
                    if 0 >= maxSum:
                        break
        return cnt