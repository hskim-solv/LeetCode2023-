class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        o = [k for k,v in Counter(arr).items() if v == 1]
        if len(o) >= k:
            return o[k-1]
        return ""
