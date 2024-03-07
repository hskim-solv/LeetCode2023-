class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        cnt_zero = s.count('0')
        return (n-cnt_zero-1)*'1'+cnt_zero*'0'+'1'