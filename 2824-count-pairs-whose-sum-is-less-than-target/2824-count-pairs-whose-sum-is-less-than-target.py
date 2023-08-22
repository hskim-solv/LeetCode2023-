class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]+nums[i] < target:
                    res+=1
                else:
                    break
            if j < i:
                break
        return res