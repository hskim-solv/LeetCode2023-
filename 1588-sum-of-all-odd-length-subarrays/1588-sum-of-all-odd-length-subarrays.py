class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = sum( ((i + 1) * (len(arr) - i) + 1) // 2 * (arr[i] + arr[-i-1])  for i in range(len(arr) // 2) )
        if len(arr) & 1:
            h = len(arr) // 2
            ans += ((h + 1) * (len(arr) - h) + 1) // 2 * (arr[h]) 
        return ans