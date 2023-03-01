class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        '''
        total = sum(nums)
        answar = []
        cum = 0
        for i, n in enumerate(nums):
            answar.append(abs(total - n - cum * 2))
            cum += n
        return answar
        '''
        left = 0
        right = sum(nums[1:])
        ans = []
        for i in range(1,len(nums)):
            ans.append(abs(left-right))
            left += nums[i-1]
            right -= nums[i]
        ans.append(left)
        return ans