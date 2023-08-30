class Solution:
    def __init__(self):
        self.d = defaultdict(int)
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort(reverse=True)
        def helper(nums,target):
            for n in nums:
                if target-n < 0:
                    continue
                if target-n == 0:
                    self.d[target] += 1
                    continue
                if target-n not in self.d:
                    self.d[target-n] = helper(nums,target-n)
                self.d[target] += self.d[target-n]
    
            return self.d[target]
        return helper(nums,target)
            