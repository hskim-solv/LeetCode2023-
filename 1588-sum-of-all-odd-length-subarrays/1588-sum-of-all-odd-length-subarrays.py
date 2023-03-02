class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        #return sum( ( (i + 1) * (len(arr) - i) + 1) // 2 * a for i, a in enumerate(arr) )
        return sum( ( (i + 1) * (len(arr) - i) + 1) // 2 * ( arr[i] if i == len(arr)//2 else arr[i] + arr[-i-1])  for i in range( (len(arr) + 1) // 2 ) )