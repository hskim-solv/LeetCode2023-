class Solution:
    def countElements(self, nums: List[int]) -> int:
        mx = max(nums)
        mn = min(nums)
        while mx in nums:
            nums.remove(mx)
        while mn in nums:
            nums.remove(mn)
        return len(nums)