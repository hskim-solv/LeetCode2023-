class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        '''
        # 1
        total, cum = sum(nums), 0
        answar = []
        for n in nums:
            answar.append(abs(total - n - cum * 2))
            cum += n
        return answar
        
        # 2
        cum = list(itertools.accumulate(nums))
        total = cum[-1]
        return [abs(total- c*2 + n) for n,c in zip(nums,cum)]
        '''
        # 3
        left, right, answar  = 0, sum(nums), []

        for n in nums:
            left += n
            answar.append(abs(right-left))
            right -= n
        return answar
        
        