class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # use DFS to parse the course structure
        self.graph = collections.defaultdict(list) # a graph for all courses
        self.res = []
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1]) 
        self.visited = [0]*numCourses # DAG detection 
        for node in range(numCourses):
            if not self.DFS(node):
                return []
             # continue to search the whole graph
        return self.res
    
    def DFS(self, node):
        if self.visited[node] == -1: # cycle detected
            return False
        if self.visited[node] == 1:
            return True # has been finished, and been added to self.res
        self.visited[node] = -1 # mark as visited
        for x in self.graph[node]:
            if not self.DFS(x):
                return False
        self.visited[node] = 1 # mark as finished
        self.res.append(node) # add to solution as the course depenedent on previous ones
        return True