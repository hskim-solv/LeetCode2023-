class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for key, cnt in Counter(arr).items():
            if cnt == 1: 
                k -= 1
                if k == 0:
                    return key
        return ""


