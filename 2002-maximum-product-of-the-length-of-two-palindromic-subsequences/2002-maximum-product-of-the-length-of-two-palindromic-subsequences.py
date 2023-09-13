class Solution:
    def maxProduct(self, s: str) -> int:
        def is_pal(l):
            return l == l[::-1]
        arr = deque(sorted([mask for mask in range(1, 1<<len(s)) if is_pal([s[i] for i in range(len(s)) if mask & (1<<i)])], key=lambda x: bin(x).count('1'), reverse=True))


        s = 1
        while arr:
            p = arr.popleft()
            bp1 = bin(p).count('1')

            for n in arr:
                if not p & n:
                    s = max(s, bp1 * bin(n).count('1'))
        return s