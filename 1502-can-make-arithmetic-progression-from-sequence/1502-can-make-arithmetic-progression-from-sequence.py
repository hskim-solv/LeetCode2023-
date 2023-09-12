class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr.pop()-arr[-1]
        for i in range(len(arr)-1):
            if arr[i]+diff!=arr[i+1]:
                return False
        return True
        
            