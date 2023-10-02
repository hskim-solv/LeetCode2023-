class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        res = set()
        for n in nums:
            for i in range(n[0],n[1]+1):
                if i not in res:
                    res.add(i)
        return len(res)