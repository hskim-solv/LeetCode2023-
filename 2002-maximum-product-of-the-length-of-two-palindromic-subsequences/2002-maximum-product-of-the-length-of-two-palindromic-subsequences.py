class Solution:
    def maxProduct(self, s: str) -> int:
        def is_pal(l):
            return l == l[::-1]
        arr = deque(sorted([mask for mask in range(1, 1<<len(s)) if is_pal([s[i] for i in range(len(s)) if mask & (1<<i)])], key=lambda x: bin(x).count('1'), reverse=True))


        result = 1
        while True:
            p = arr.popleft()
            if bin(p).count('1') ** 2 <= result: 
                break
            for n in arr:
                if not p & n:
                    if bin(p).count('1') * bin(n).count('1') > result:
                        result = bin(p).count('1') * bin(n).count('1')
                        break
        return result