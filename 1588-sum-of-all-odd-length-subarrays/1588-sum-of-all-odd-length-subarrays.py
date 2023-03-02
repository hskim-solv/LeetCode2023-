class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        la =len(arr)
        h = la//2
        return  ( (h + 1) * ceil(la/2) + 1) // 2 * (arr[h] if la & 1 else 0) + sum( 
            (  (i + 1) * (la - i) + 1 ) // 2 * 
            (arr[i] + arr[-i-1])  
            for i in range( h ) 
       )