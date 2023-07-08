class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target == nums[-1]:
            return len(nums)-1
        if target <= nums[0]:
            return 0
        if len(nums) == 2:
            return 1
        start, end = 0, len(nums)-1
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