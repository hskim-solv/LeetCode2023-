class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, [k for k, v in Counter(nums).items() if v == 2], 0)
        