class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        answar = []
        cum = 0
        for n in nums:
            answar.append(abs(total - n - cum * 2))
            cum += n
        return answar
        '''
        # 2
        cum = list(itertools.accumulate(nums))
        total = cum[-1]
        return [abs(total- c*2 + n) for n,c in zip(nums,cum)]
        # 3
        left = 0
        right = sum(nums)
        ans = []
        for n in nums:
            left += n
            ans.append(abs(left-right))
            right -= n
        return ans
        '''
        