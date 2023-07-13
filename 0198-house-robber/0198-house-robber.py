class Solution:
    def rob(self, nums: List[int]) -> int:
        self.d = {}
        def inner(nums,idx):
            if not nums:
                return 0
            if len(nums) < 3:
                return max(nums)
            if idx not in self.d:
                self.d[idx] = nums[0]+max(inner(nums[2:],idx+2),inner(nums[3:],idx+3))
            return self.d[idx]
        return max(inner(nums,0),inner(nums[1:],1))