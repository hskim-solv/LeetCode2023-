class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(set(nums)) < 3:
            return False
        mn1 = min(nums)
        
        i = nums.index(min(nums))
        #print(mn1,i,len(nums))
        if len(set(nums[i:])) < 3:
            #print(mn1,i,len(nums))
            ni = nums[i]
            del nums[i]
            while i < len(nums) and ni == nums[i]:
                del nums[i]
            i = nums.index(min(nums))
            return self.increasingTriplet(nums)
        else:
            if mn1 < max(nums[i+1:]):
                k = nums.index(max(nums[i+1:]))
                if len(set(nums[i:k+1])) < 3:
                    #print(nums,'k')
                    return any([self.increasingTriplet(nums[i:k]+nums[k+1:]),self.increasingTriplet(nums[:k+1])])
                elif mn1 < max(nums[i+1:k]):
                    return True
            
        mx1 = max(nums)
        j = nums.index(mx1)
        if len(set(nums[:j+1])) < 3:
            nj=nums[j]
            del nums[j]
            while 0 < j and nj == nums[j]:
                del nums[j]
            #print(nums,'j')
            return self.increasingTriplet(nums)
        else:
            if min(nums[:j]) < mx1:
                i = nums.index(min(nums[:j]))
                if len(nums[i:j+1]) < 3:
                    #print(nums,'ij')
                    return any([self.increasingTriplet(nums[:i]+nums[i+1:j+1]),self.increasingTriplet(nums[i:])])
                elif mn1 < max(nums[i+1:k]):
                    return True
     
        