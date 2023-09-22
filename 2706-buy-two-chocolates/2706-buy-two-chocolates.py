class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort(reverse=True)
        return money if sum(prices[-2:]) > money else money-sum(prices[-2:])
            