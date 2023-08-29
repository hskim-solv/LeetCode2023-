class Solution:
    def magicalString(self, n: int) -> int:
        def gen():
            for x in (1, 2, 2):
                yield x
            for i, x in enumerate(gen()):
                if i > 1:
                    for _ in range(x):
                        yield i % 2 + 1
        return sum(x & 1 for x in islice(gen(), n))