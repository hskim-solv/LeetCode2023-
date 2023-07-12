class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = 0
        d2 = {}
        for k1,v1 in Counter(nums1).items():
            for k2,v2 in Counter(nums2).items():
                if k1+k2 not in d2:
                    d2[k2+k1] = 0
                d2[k2+k1] += v1*v2
        d3={}
        for k2,v2 in d2.items():
            for k3,v3 in Counter(nums3).items():
                if k3+k2 not in d3:
                    d3[k2+k3] = 0
                d3[k2+k3] += v3*v2
        c4 = Counter(nums4)
        for k3,v3 in d3.items():
                if -k3 in c4:
                    cnt += c4[-k3]*v3

        return cnt