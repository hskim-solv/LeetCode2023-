class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)-1
        maxi = 0
        i = 0
        j = -1
        flag = 0

        while j < n:
            j += 1
            if nums[j] > threshold:
                if flag == 1:
                    flag = 0
                    j -= 1
                continue
            if flag == 0:
                if nums[j] % 2 == 0:
                    i = j
                    maxi = max(maxi, j-i+1)
                    flag = 1
            elif flag == 1:
                if (nums[j-1]+nums[j]) % 2:
                    maxi = max(maxi, j-i+1)
                else:
                    flag = 0
                    j -= 1
            

        return maxi