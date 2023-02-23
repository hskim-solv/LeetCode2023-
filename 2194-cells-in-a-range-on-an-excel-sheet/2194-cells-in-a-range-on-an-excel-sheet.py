class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s0, s1, _, s3, s4 = map(ord, s)
        return [chr(x) + chr(y) for x in range(s0, s3 + 1) for y in range(s1, s4 + 1)]


               