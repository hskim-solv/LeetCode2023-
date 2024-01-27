class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = defaultdict(int)
        cnt = len(nums)
        i = 0
        while i != cnt:
            
            if d[nums[i]] > 1:
                nums.remove(nums[i])
                cnt -= 1
            else:
                d[nums[i]] += 1
                i += 1
        return cnt