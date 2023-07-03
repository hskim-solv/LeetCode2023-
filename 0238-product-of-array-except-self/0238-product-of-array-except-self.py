class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total = reduce(lambda x, y: x * y, nums, 1)
        for i in range(len(nums)):
            if not total:
                if not nums[i]:
                    nnl = nums[:i] + nums[i+1:]
                    if 0 not in nnl:
                        res.append(reduce(lambda x, y: x * y, nnl, 1))
                        continue
                res.append(total)
            else:
                res.append(total//nums[i])
        return res