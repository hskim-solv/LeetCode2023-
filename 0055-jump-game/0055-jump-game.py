class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        jumps = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > jumps:
                jumps = 0
            else:
                jumps += 1
        return nums[0] > jumps