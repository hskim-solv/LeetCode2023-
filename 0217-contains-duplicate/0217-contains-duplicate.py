class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        return sorted(set(nums)) != nums