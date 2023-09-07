class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high+1):
            if len(str(i)) % 2:
                continue
            s = str(i)
            m = len(s)//2
            if sum( map(int, s[:m]) ) == sum( map(int, s[m:]) ):
                res += 1
        return res