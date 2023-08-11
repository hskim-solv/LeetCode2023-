class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        tmp = [nums.pop(0),None]
        for n in nums+[None]:
            if tmp[0] + 1 == n or (tmp[-1] and tmp[-1] + 1 == n):
                tmp[-1] = n
            else:
                if tmp[-1]:
                    res.append("->".join([str(tmp[0]),str(tmp[-1])]))
                else:
                    res.append(str(tmp[0]))
                tmp = [n, None]

        return res