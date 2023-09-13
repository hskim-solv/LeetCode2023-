class Solution:
    def maxProduct(self, s: str) -> int:
        def is_pal(l):
            return l == l[::-1]
        arr = sorted([mask for mask in range(1, 1<<len(s)) if is_pal([s[i] for i in range(len(s)) if mask & (1<<i)])], key=lambda x: bin(x).count('1'), reverse=True)


        result = 1
        for i in range(len(arr)):
            if bin(arr[i]).count('1') ** 2 <= result: 
                break
            for j in range(i+1, len(arr)):
                if not arr[i] & arr[j]:
                    if bin(arr[i]).count('1') * bin(arr[j]).count('1') > result:
                        result = bin(arr[i]).count('1') * bin(arr[j]).count('1')
                        break
        return result