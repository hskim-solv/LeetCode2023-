class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(set(nums)) < 3:
            return False

        i = nums.index(min(nums))
        #print(i,nums)
        if len(set(nums[i:])) < 3:
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                #print(nums)
                del nums[i+1]
            del nums[i]
            return self.increasingTriplet(nums)
    
        else:
            if nums[i] < max(nums[i+1:]):
                k = nums.index(max(nums[i+1:]))
                if len(set(nums[i:k+1])) < 3:
                    #print(nums,'k')
                    return any([self.increasingTriplet(nums[i:k]+nums[k+1:]),self.increasingTriplet(nums[:k+1])])
                elif nums[i] < max(nums[i+1:k]):
                    return True
            
        mx1 = max(nums)
        j = nums.index(mx1)
        if len(set(nums[:j+1])) < 3:
            while j < len(nums) and nums[j] == nums[j+1]:
                del nums[j+1]
            del nums[j]
            return self.increasingTriplet(nums)
        else:
            if min(nums[:j]) < mx1:
                i = nums.index(min(nums[:j]))
                if len(set(nums[i:j+1])) < 3:
                    #print(nums,'ij')
                    return any([self.increasingTriplet(nums[:i]+nums[i+1:j+1]),self.increasingTriplet(nums[i:])])
                elif mn1 < max(nums[i+1:k]):
                    return True
     
        