class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        cnt = 0 
        while nums.pop() < k:
            cnt += 1
        return cnt