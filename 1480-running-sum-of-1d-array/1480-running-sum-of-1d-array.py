class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        box = 0
        for n in nums:
            box += n
            result.append(box)
        return result