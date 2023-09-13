class Solution:
    def maxProduct(self, s: str) -> int:
        def is_pal(l):
            while len(l) > 1:
                if l.popleft() != l.pop():
                    return False
            return True
        arr = sorted([mask for mask in range(1, 1<<len(s)) if is_pal(deque([s[i] for i in range(len(s)) if mask & (1<<i)]))], key=lambda x: bin(x).count('1'))
        res = 1
        while arr:
            p = arr.pop()
            if bin(p).count('1') ** 2 <= res: 
                return res
            for n in arr:
                if not p & n:
                    res = max(res, bin(p).count('1') * bin(n).count('1'))