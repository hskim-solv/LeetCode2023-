class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i,j = 0,1
        
        res = [0] * len(nums)
        for n in nums:
            if n > 0:
                res[i] = n
                i += 2
            else:
                res[j] = n
                j += 2

        return res