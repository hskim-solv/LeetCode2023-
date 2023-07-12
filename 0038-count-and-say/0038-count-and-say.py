class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        ss = list(self.countAndSay(n-1))
        head = ss[-1]
        cnt = 0
        res = ""
        while ss:
            s = ss.pop()
            if s == head:
                cnt += 1
            else:
                res = str(cnt) + head + res
                head = s
                cnt = 1
        if cnt != 0:
            res = str(cnt) + head + res
        return res
    