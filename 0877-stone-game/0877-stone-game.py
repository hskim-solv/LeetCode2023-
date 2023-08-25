class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        i = 0
        res = 0
        piles = deque(piles)
        while piles:
        
            if piles[0] < piles[-1]:
                if i % 2:
                    res -= piles.pop()
                else:
                    res += piles.pop()
            else:
                if i % 2:
                    res -= piles.popleft()
                else:
                    res += piles.popleft()
        return res > 0