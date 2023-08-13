class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(graph, path):
            node = path[-1]

            if node == n:
                res.append(path)
            else:
                for sub in graph[node]:
                    dfs(graph,path+[sub]) 
        n = len(graph)-1
        res = []
        dfs(graph, [0])
        return res
        
                
