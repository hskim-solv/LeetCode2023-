class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = 0
        while len(nums) > 2:
            i = nums.pop() 
            if i - diff in nums:
                if i - diff*2 in nums:
                    n += 1
        return n

            