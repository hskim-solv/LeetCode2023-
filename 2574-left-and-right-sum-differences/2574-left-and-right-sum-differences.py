class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        '''
        total = sum(nums)
        answar = []
        cum = 0
        for n in nums:
            answar.append(abs(total - cum * 2 - n))
            cum += n
        return answar
        '''
        cum = list(itertools.accumulate(nums))
        total = cum[-1]
        print(total)
        return [abs(total-c*2 + n) for n,c in zip(nums,cum)]
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
        '''