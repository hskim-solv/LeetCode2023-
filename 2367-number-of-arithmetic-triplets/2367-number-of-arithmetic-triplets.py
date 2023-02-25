class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = 0
        while len(nums) > 2:
            i = nums.pop() -diff
            if i in nums:
                if i - diff in nums:
                    n += 1
        return n

            