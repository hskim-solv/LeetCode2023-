class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = deque(range(1,m+1))
        for i in range(len(queries)):
            idx = P.index(queries[i])
            P.remove(queries[i])
            P.appendleft(queries[i])
            queries[i] = idx
        return queries
            