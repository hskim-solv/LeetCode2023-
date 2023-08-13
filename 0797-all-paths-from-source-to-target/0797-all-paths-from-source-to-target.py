class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(graph, path):
            node = path[-1]

            for sub in graph[node]:
                if sub == n:
                    res.append(path+[sub])
                else:
                    dfs(graph,path+[sub]) 
        n = len(graph)-1
        res = []
        dfs(graph, [0])
        return res
        
                
