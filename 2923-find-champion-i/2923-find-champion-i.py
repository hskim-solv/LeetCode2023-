class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        cnt_victory = list(map(sum,grid))
        return cnt_victory.index(max(cnt_victory))