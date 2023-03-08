class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}
        nums2 = deque(nums2)
        while nums2:
            n = nums2.popleft()
            if n in nums1:
                i = nums1.index(n)
                for n2 in nums2:
                    if n < n2:
                        ans[i] = n2
                        break
                if i not in ans:
                    ans[i] = -1

        return [ v for k, v in sorted(ans.items(), key= lambda item: item[0])]


'''
            for n1 in nums1:
                for i in range(nums2.index(n1), l):
                    if nums2[i] > n1:
                        ans.append(nums2[i])
                        break
                    if i == l-1:
                        ans.append(-1)
        return ans'''
            