class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        keys1 = set(nums1)
        keys2 = set(nums2)
        cnt1 = 0
        cnt2 = 0
        for key in keys1:
            if key in keys2:
                cnt1 += nums1.count(key)
        for key in keys2:
            if key in keys1:
                cnt2 += nums2.count(key)
        return [cnt1,cnt2]