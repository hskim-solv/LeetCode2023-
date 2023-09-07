class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = {tuple(),tuple(nums)}
        for i in range(1,len(nums)):
            res.update(set(map(tuple, map(sorted, combinations(nums, i)))))

        return res