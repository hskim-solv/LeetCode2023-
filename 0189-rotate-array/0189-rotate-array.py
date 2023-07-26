class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        for _ in range(k % len(nums)):
            nums.insert(0,nums.pop())
        """
        """
        k = len(nums) - k % len(nums)
        nums[.extend(nums[:k])]
        del nums[:k]

        """
        k = len(nums) - k % len(nums)
        nums[k:], nums[:k] = nums[k:][::-1], nums[:k][::-1]
        nums.reverse()
