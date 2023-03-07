class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dtt, trash = [], []
        i = 0

        ox = Counter(arr)
        for ist in arr:
            if ox[ist] == 1:
                i += 1
                if i == k:
                    return ist
            del ox[ist]
            if not ox:
                return ""
            