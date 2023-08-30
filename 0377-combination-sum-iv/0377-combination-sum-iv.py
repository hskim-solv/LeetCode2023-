class Solution:
    def __init__(self):
        self.d = defaultdict(int)
        self.d[0] = 1
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target in self.d:
            return self.d[target]
        if target < 0:
            return 0
        for n in nums[::-1]:
            
            if target-n not in self.d:
                self.d[target-n] = self.combinationSum4(nums,target-n)
            self.d[target] += self.d[target-n]
    
        return self.d[target]
            