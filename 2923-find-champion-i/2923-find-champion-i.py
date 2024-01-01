class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        vic_top = 0
        top_team = 0
        n = len(grid)
        
        for i in range(n):
            cnt_vic = 0
            for j in range(n):
                if grid[i][j]:
                    cnt_vic += 1
                
            if vic_top < cnt_vic:
                vic_top = cnt_vic
                top_team = i
            #print(top_team,vic_top,cnt_vic)
        return top_team
