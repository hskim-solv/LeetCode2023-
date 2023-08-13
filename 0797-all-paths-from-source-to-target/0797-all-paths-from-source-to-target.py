class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(graph, path):
            for sub in graph[path[-1]]:
                if sub == n:
                    res.append(path+[sub])
                else:
                    dfs(graph,path+[sub]) 
        n = len(graph)-1
        res = []
        dfs(graph, [0])
        return res
        
                
