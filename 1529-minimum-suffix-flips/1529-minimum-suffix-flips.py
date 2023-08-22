class Solution:
    def minFlips(self, target: str) -> int:
        #print(target.split('0'))
        return max(0,len(list(filter(None, target.split('0'))))*2) - (target[-1]=='1')