class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = {tuple()}
        for i in range(1,len(nums)+1):
            res.update(set(map(tuple, map(sorted, combinations(nums, i)))))
        return res