class Solution:
    def minFlips(self, target: str) -> int:
        return max(0,len(list(filter(None, target.split('0'))))*2) - int(target[-1])