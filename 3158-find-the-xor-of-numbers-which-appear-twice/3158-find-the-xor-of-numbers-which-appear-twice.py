class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res = []
        for k, v in Counter(nums).items():
            if v == 2:
                res.append(k)
        if res:
            return reduce(lambda x, y: x ^ y, res)
        return 0