class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(list)
        for i,n in enumerate(nums):
            d[n].append(i)
            if len(d[n]) > 1:
                if abs(d[n][-2]-d[n][-1]) <= k:
                    return True
        return False
                