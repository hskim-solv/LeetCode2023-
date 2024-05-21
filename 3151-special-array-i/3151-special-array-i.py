class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        is_even = nums[0] & 1
        for i in range(1, len(nums)):
            if is_even:
                if nums[i] & 1 == 0:
                    is_even = 0
                else:
                    return False
            else:
                if nums[i] & 1 != 0:
                    is_even = 1
                else:
                    return False
        return True