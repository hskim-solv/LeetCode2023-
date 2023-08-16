class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        #diff = [n1-n0 for n1,n0 in zip(nums[:-1],nums[1:])]
        for i in range(len(l)):
  
            e = set(nums[l[i]:r[i]+1])
            if len(e) == 1:
                res.append(True)
                continue
            if len(e) != r[i]-l[i]+1:
                res.append(False)
                continue
            e = sorted(e)
            top = e.pop()
            diff = top - e[-1]
            while e:
                if diff != top-e[-1]:
                    res.append(False)
                    break
                top = e.pop()
            if not e:
                res.append(True)

        return res
                    