class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort(reverse=True)
        total = sum(prices[-2:])
        return money if total > money else money-total
            