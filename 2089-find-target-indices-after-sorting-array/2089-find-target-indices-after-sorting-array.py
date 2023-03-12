class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums.sort()
        while target in nums:
            res.append(nums.index(target)+len(res))
            nums.remove(target)
        return res