class Solution:
    def sortString(self, s: str) -> str:
        res = ""
        s = deque(sorted(s))

        ss = deque(sorted(set(s)))

        while s:

            for ch in ss:
                if ch in s:
                    res += ch
                    s.remove(ch)
            s.reverse()
            ss.reverse()

        return res    