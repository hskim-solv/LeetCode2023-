class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        n = len(grid)
        for i in range(n - 2):
            result.append([])
            for j in range(n - 2):
                result[i].append( max(max(grid[i+x][j:j+3]) for x in range(3)))

        return result

