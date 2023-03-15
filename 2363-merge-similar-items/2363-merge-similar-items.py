class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = {}
        for v, w in items1 + items2:
            if v in d:
                d[v] += w
            else:
                d[v] = w
        return sorted(d.items())