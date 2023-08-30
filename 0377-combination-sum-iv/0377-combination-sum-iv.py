class Solution:
    def __init__(self):
        self.d = defaultdict(int)
    def combinationSum4(self, nums: List[int], target: int) -> int:
        for n in nums:
            print(target,n)
            if target-n > 0:
                if target-n not in self.d:
                    self.d[target] += self.combinationSum4(nums,target-n)
                else:
                    self.d[target] += self.d[target-n]
            elif target-n == 0:
                self.d[target] += 1

        
        return self.d[target]
            