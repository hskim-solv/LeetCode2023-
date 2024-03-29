class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(n):
            for i in range(2, n):
                if (n % i) == 0:
                    return False
            return True
        for i in range(len(nums)-2, -1, -1):
            if nums[i+1] <= nums[i]:
                for p in range(max(2,nums[i]-nums[i+1]+1), nums[i]):
                    if is_prime(p):
                        nums[i] -= p
                        break
                if nums[i+1] <= nums[i]:
                    return False
        return True