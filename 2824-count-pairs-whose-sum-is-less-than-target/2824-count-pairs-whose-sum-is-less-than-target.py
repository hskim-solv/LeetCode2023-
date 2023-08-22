class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)-1):
            
            tn = target-nums[i]

            for j in range(i+1,len(nums)):
                if nums[j] < tn:
                    res+=1
                else:
                    break
        return res