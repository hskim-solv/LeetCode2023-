class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        for n1 in nums1:
            for n2 in nums2:
                n2 *= k
                if n1 % n2 == 0:
                    res += 1
        return res