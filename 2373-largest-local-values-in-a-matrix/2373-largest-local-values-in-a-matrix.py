class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result =[]
        n = len(grid)
        for i in range(n - 2):
            row = []
            for j in range(n - 2):
                ij =[]
                for x in range(3):
                    ij.append(max(grid[i + x][j : j + 3]))
                row.append(max(ij))
            result.append(row)
        return result

