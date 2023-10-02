class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)-1
        maxi = 0
        i = 0
        j = -1
        flag = False

        while j < n:
            j += 1
            if nums[j] > threshold:
                if flag:
                    flag = False
                    j -= 1
                continue
            if flag:
                if (nums[j-1]+nums[j]) % 2:
                    maxi = max(maxi, j-i+1)
                else:
                    flag = 0
                    j -= 1
            else:
                if nums[j] % 2 == 0:
                    i = j
                    maxi = max(maxi, j-i+1)
                    flag = 1


            

        return maxi