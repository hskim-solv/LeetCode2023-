class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)-1
        maxi = 0
        j = -1
        flag = False

        while j < n:
            j += 1
            if nums[j] > threshold:
                if flag:
                    flag = not flag
                    j -= 1
                continue
                
            if nums[j] % 2:
                if flag:
                    if nums[j-1] % 2 == 0:
                        maxi = max(maxi, j-i+1)
                    else:
                        flag = not flag
                        j -= 1
            else:
                if flag:
                    if nums[j-1] % 2:
                        maxi = max(maxi, j-i+1)
                    else:
                        flag = not flag
                        j -= 1
                else:
                    i = j
                    maxi = max(maxi, 1)
                    flag = not flag

        return maxi