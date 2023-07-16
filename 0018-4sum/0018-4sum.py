class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        nums.sort()
        
        for i in range(len(nums)-3):
            if i == 0 or nums[i] != nums[i-1]:
                threeResult = self.threeSum(nums[i+1:], target-nums[i])
                for item in threeResult:
                    results.append([nums[i]] + item)
        return results
                
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        length = len(nums)-1
        for i in range(length-1):
            l, r = i + 1, length
            t = target - nums[i]
            if i == 0 or nums[i] != nums[i-1]:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == t:
                        results.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]: l += 1
                        while l < r and nums[r] == nums[r-1]: r -= 1
                        l += 1; r -=1
                    elif s < t:
                        l += 1
                    else:
                        r -= 1
        return results