class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(int)
        for i,n in enumerate(nums, 1):
            if d[n]:
                if abs(d[n]-i) <= k:
                    return True
            d[n] = i
        return False
                