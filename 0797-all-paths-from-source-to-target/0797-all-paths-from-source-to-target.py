class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(path):
            if path[-1] == n:
                res.append(path)
            else:
                for sub in graph[path[-1]]:
                    dfs(path+[sub]) 
        n = len(graph)-1
        res = []
        dfs([0])
        return res
        
                
