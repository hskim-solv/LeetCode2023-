class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = defaultdict(str)
        for ss,tt in zip(s,t):
            if ss not in d:
                if tt in d.values():
                    return False
                d[ss] = tt
            else:
                if d[ss] != tt:
                    return False

        return True