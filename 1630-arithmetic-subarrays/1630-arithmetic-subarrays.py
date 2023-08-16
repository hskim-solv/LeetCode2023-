class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            e = sorted(nums[l[i]:r[i]+1])
            f = e.pop()
            diff = f - e[-1]
            while e:
                print(e,diff,'in')
                if diff  != f-e[-1]:
                    res.append(False)
                    break
                f = e.pop()
            print(e,diff)
            if not e:
                res.append(True)

        return res
                    