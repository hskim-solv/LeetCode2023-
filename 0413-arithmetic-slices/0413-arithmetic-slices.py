class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        res = 0
        step = 0
        while len(nums) > 2:
            node = nums.pop()
            if node-nums[-1] == nums[-1]-nums[-2]:
                step += 1
                res += step
            else:
                step = 0
        return res
            
                
        