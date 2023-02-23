class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        result = 0
        while nums:
            num = nums.pop()
            result += num
            while num:
                num, digit = divmod(num, 10)
                result -= digit
        return result
                
                