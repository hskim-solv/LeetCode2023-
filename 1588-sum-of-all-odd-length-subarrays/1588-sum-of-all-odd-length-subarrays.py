class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        return  ( (len(arr) // 2 + 1) * (len(arr) - len(arr) // 2) + 1) // 2 * (arr[len(arr) // 2] if len(arr) & 1 else 0) + sum( 
            (  (i + 1) * (len(arr) - i) + 1 ) // 2 * 
            (arr[i] + arr[-i-1])  
            for i in range( len(arr) // 2 ) 
       )