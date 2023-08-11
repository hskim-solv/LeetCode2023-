class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        tmp = [nums.pop(0)]
        for n in nums:
            if tmp[-1]+1 == n:
                tmp.append(n)
            else:
                if len(tmp) > 1:
                    res.append("->".join([str(tmp[0]),str(tmp[-1])]))
                else:
                    res.append(str(tmp[0]))
                tmp = []
                tmp.append(n)
        if tmp:
            if len(tmp) > 1:
                res.append("->".join([str(tmp[0]),str(tmp[-1])]))
            else:
                res.append(str(tmp[0]))
        return res