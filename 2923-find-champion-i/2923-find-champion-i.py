class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)-1
        for i in range(n+1):
            if sum(grid[i]) == n:
                return i