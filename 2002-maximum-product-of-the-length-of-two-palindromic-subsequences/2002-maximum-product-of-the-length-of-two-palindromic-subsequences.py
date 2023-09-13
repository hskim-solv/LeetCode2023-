class Solution:
    def maxProduct(self, s: str) -> int:
        def is_pal(l):
            return l == l[::-1]
        arr =   sorted([mask for mask in range(1, 1<<len(s)) if is_pal([s[i] for i in range(len(s)) if mask & (1<<i)])], key=lambda x: bin(x).count('1'))
        s = 1
        while arr:
            p = arr.pop()
            bp1 = bin(p).count('1')
            if bp1 ** 2 <= s: 
                return s
            for n in arr:
                if not p & n:
                    s = max(s, bp1 * bin(n).count('1'))
        return s