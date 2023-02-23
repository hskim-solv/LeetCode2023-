class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        return [chr(x)+str(y) for x in range(ord(s[0]),ord(s[-2])+1) for y in range(int(s[1]),int(s[-1])+1)]


               