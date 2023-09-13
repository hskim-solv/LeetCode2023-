class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 2:
            res = set()
            for i in range(1, 10-k):
                res.add(int(str(i)+str(i+k)))
            for i in range(max(1, k), 10):
                res.add(int(str(i)+str(i-k)))
            return res
        res = set()
        for num in self.numsSameConsecDiff(n-1, k):
            num = str(num)
            c = int(num[-1])
            if c+k < 10:
                res.add(int(num+str(c+k)))
            if c-k >= 0:
                res.add(int(num+str(c-k)))
        return res