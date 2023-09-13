class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        def is_pal(l):
            return l == l[::-1]
        arr = sorted([mask for mask in range(1, 1<<n) if is_pal(list(compress(s, map(int, bin(mask)[:1:-1]))))], key=lambda x: bin(x).count('1'))
        res = 1
        while arr:
            p = arr.pop()
            if bin(p).count('1') ** 2 <= res: 
                return res
            for n in arr:
                if not p & n:
                    res = max(res, bin(p).count('1') * bin(n).count('1'))