class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return reduce(max, map(sum, accounts))
        