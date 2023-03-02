class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        return sum(max(m) for m in zip(*map(sorted, grid)))
