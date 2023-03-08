class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        l = len(nums2)
        for n1 in nums1:
            for i in range(nums2.index(n1), l):
                if nums2[i] > n1:
                    ans.append(nums2[i])
                    break
                if i == l-1:
                    ans.append(-1)
        return ans
            