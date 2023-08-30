class Solution:
    def __init__(self):
        self.d = defaultdict(int)
        self.d[0] = 1
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        for n in nums[::-1]:
            if target-n < 0:
                continue
            if target-n not in self.d:
                self.d[target-n] = self.combinationSum4(nums,target-n)
            self.d[target] += self.d[target-n]
    
        return self.d[target]
            