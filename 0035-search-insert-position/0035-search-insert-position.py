class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        end = len(nums)
        if target > nums[-1]:
            return end
        if target == nums[-1]:
            return end-1
        if end == 2:
            return 1
        start = 0
        mid = end // 2
        while end - start > 1:
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid
                if nums[mid-1] < target:
                    return mid
            elif nums[mid] < target:
                start = mid
                if target <= nums[mid+1]:
                    return mid+1
            mid = (start + end)//2
        return mid