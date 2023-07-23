class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        if not n: return 0
        lg = int(log(n,5))
        while lg:
            res += n // (5 ** lg)
            lg -= 1
        return res
