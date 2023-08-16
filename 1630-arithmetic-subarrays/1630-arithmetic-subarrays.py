class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            e = set(nums[l[i]:r[i]+1])
            if len(e) == 1:
                res.append(True)
                continue
            if len(e) != r[i]-l[i]+1:
                print(e,nums[l[i]:r[i]+1],r[i]-l[i])
                res.append(False)
                continue
            mx, mn = max(e), min(e)
            #print(mx-mn,len(e))
            diff, mod = divmod(mx-mn,r[i]-l[i])
            if mod:
                #print('mod')
                res.append(False)
                continue
            while mn in e:
                #print(mn,e)
                e.remove(mn)
                mn += diff
            

            if not e:
                res.append(True)
            else:
                res.append(False)

        return res
                    