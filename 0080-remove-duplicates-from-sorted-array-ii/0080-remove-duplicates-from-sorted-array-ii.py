class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = defaultdict(int)
        cnt = len(nums)
        i = 0
        while i != cnt:
            d[nums[i]] += 1
            if d[nums[i]] > 2:
                nums.remove(nums[i])
                cnt -= 1
            else:
                i += 1
        return cnt