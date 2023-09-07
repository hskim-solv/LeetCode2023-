class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        print(piles)
        l = len(piles)
        res = 0
        print(l//3)
        for i in range(l//3, l ,2 ):
            res += piles[i]
            print(res)
        return res