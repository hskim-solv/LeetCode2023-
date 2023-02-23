from itertools import permutations
class Solution:
    def minimumSum(self, num: int) -> int:
        ssn = sorted(str(num))

        return int(ssn[0] + ssn[2]) + int(ssn[1] + ssn[3])
    