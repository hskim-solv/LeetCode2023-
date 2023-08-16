class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            e = set(nums[l[i]:r[i]+1])
            if len(e) == 1:
                res.append(True)
                continue
            if len(e) != r[i]-l[i]+1:
                res.append(False)
                continue
            mn = min(e)
            diff, mod = divmod(max(e)-mn,r[i]-l[i])
            if mod:
                res.append(False)
                continue
            while mn in e:
                e.remove(mn)
                mn += diff
            
            if e:
                res.append(False)
            else:
                res.append(True)

        return res
                    