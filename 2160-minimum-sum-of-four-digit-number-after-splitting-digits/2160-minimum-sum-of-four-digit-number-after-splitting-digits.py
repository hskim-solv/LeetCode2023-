from itertools import permutations
class Solution:
    def minimumSum(self, num: int) -> int:
        l = []
        while num:
            num, digit = divmod(num, 10)
            l.append(digit)
        l.sort()
        return (l[0]+l[1])*10 + l[2] + l[3]