class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = [sum(row) for row in mat]
        mx = max(res)
        return [res.index(mx),mx]