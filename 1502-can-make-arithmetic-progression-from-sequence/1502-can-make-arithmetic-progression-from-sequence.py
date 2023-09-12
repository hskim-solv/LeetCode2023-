class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = min(arr)
        arr.remove(n)
        m = min(arr)
        arr.remove(m)
        diff = m-n
        m += diff
        while arr and m in arr:
            arr.remove(m)
            m += diff
            
        return not bool(arr)
        
            