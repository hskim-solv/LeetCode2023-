class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        o = list(k for k, v in Counter(arr).items() if v == 1)
        return o[k-1] if len(o) > k-1 else ""

