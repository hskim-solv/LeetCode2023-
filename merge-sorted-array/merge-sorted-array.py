class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        m -= 1
        for n2 in nums2:
            for i in range(i, m + n + 1):
                if nums1[i] > n2 or i > m:
                    nums1.insert(i, n2)
                    del nums1[-1]
                    m += 1
                    i += 1
                    break
