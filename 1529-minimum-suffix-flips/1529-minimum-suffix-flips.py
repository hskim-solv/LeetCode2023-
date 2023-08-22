class Solution:
    def minFlips(self, target: str) -> int:
        if '1' not in target:
            return 0
        return len(list(filter(None, target.split('0'))))*2 - int(target[-1])