class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        thieves = [(i, j) for j in range(n) for i in range(n) if grid[i][j]]

        visited = [[0 for _ in range(n)] for _ in range(n)]
        distance = [[0 for _ in range(n)] for _ in range(n)]

        # find the minimum mahatten distance of each cell to theives 
        depth = 0
        edge = (-1, n)
        while thieves:
            B = set()
            for i, j in thieves:
                
                if visited[i][j]:
                    continue
                    
                visited[i][j], distance[i][j] = 1, depth
                
                for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    if x not in edge and y not in edge:
                        B.add((x, y))
            thieves = B
            depth += 1

        # start from 0,0 and use dijkstra
        visited = [[0 for _ in range(n)] for _ in range(n)]
        pq = [(-distance[0][0], 0, 0)]

        while pq:
            dis, i, j = heapq.heappop(pq)
            
            if visited[i][j]:
                continue
                
            if i == n-1 and j == n-1:
                return -dis
            
            visited[i][j] = 1

            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if x not in edge and y not in edge:
                    heapq.heappush(pq, (-min(-dis, distance[x][y]), x, y))
        return -1