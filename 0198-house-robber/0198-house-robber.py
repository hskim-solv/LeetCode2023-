class Solution:
    def rob(self, nums: List[int]) -> int:
        self.d = {}
        def inner(idx):
            if len(nums)-idx == 0:
                return 0
            if len(nums)-idx < 3:
                return max(nums[idx:])
            if idx not in self.d:
                self.d[idx] = nums[idx]+max(inner(idx+2),inner(idx+3))
            return self.d[idx]
        return max(inner(0),inner(1))