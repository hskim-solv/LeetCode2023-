class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        j = 0
        s1 = deque([])
        s2 = deque([])
        for i in range(len(nums)):

            if nums[i] > 0:
                s1.append(nums[i])
            else:
                s2.append(nums[i])
            
        while s1 and s2:
            nums[j] = s1.popleft()
            nums[j+1] = s2.popleft()
            j += 2
        return nums