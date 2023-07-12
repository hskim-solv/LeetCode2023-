class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = 0
        d = defaultdict(int)
        for k1,v1 in Counter(nums1).items():
            for k2,v2 in Counter(nums2).items():
                d[k2+k1] += v1*v2
        for k4,v4 in Counter(nums4).items():
            for k3,v3 in Counter(nums3).items():
                cnt += d[0-(k4+k3)]*v4*v3

        return cnt