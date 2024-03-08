class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        f = target[-1]
        res = f*["Push"]
        f -= 1
        while f != 0:
            if f not in target:
                res.insert(f,"Pop")
            f -= 1
        return res