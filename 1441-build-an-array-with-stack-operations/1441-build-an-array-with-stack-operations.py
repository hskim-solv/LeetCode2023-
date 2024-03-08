class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        f = target.pop()
        res = f*["Push"]
        f -= 1
        while f:
            if f not in target:
                res.insert(f, "Pop")
            else:
                target.remove(f)
            f -= 1
        return res