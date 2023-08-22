class Solution:
    def minFlips(self, target: str) -> int:
        return max(0,len( " ".join( target.split('0') ).split() )*2) - (target[-1]=='1')