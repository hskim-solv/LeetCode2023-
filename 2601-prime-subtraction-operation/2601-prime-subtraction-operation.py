class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        nums = nums[::-1]
        m = nums[0]
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2,n):
                if (n % i) == 0:
                    return False
            return True
        for i in range(1, len(nums)):
            if nums[i-1] <= nums[i]:
                for p in range(nums[i]-nums[i-1]+1, nums[i]):
                    if is_prime(p):
                        nums[i] -= p
                        break
                if nums[i-1] <= nums[i]:
                    return False
        return True