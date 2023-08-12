class Solution:
    def __init__(self):
        self.cache = defaultdict(int)
        self.cache[1] = 0
    def minOperations(self, n: int) -> int:
        if n not in self.cache:
            div, mod = divmod(n,2)
            if not mod and not div:
                self.cache[n-1] = div*2 + self.minOperations(n-2)
            self.cache[n] = div + self.minOperations(n-1)

        return self.cache[n]