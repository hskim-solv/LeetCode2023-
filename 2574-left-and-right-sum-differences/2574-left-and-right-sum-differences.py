class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        answar = []
        cum = 0
        for i, n in enumerate(nums):
            a_i = total - n - cum * 2
            answar.append(abs(a_i))
            cum += n
        return answar
            