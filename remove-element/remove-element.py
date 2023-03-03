class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        output = len(nums) - nums.count(val)
        while val in nums[:output]:
            nums.remove(val)
        return output