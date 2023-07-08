class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start, end = 0, len(nums)-1
        if target == nums[0]:
            return 0
        elif target == nums[-1]:
            return end

        mid = end//2
        while end - start > 1:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
                mid = (start+end)//2
            else:
                start = mid
                mid = (start+end)//2+1
        return -1