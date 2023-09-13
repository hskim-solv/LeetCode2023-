class Solution:
    def maxProduct(self, s: str) -> int:
        def is_pal(l):
            return l == l[::-1]
        arr = [(bin(mask).count('1'), mask) for mask in range(1, 1<<len(s)) if is_pal([s[i] for i in range(len(s)) if mask & (1<<i)])]

        arr.sort(reverse=True)

        result = 1
        for i in range(len(arr)):
            if arr[i][0] ** 2 <= result: 
                break
            for j in range(i+1, len(arr)):
                if not arr[i][1] & arr[j][1]:
                    if arr[i][0] * arr[j][0] > result:
                        result = arr[i][0] * arr[j][0]
                        break
        
        return result