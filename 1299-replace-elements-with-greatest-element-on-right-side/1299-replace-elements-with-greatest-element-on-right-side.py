class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = arr.pop()
        i = -1
        n = len(arr)
        while -i <= n:
            if arr[i] > mx:
                mx, arr[i] = arr[i], mx
            else:
                arr[i] = mx
            i -= 1
        arr.append(-1)
        return arr