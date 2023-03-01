class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        answar = []
        cum = 0
        for i, n in enumerate(nums):
            answar.append(abs(total - n - cum * 2))
            cum += n
        return answar
            