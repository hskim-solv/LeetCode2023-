class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            e = nums[l[i]:r[i]+1]
            mx,mn = max(e), min(e)
            diff,mod = divmod(mx-mn,r[i]-l[i])
            if mod:
                res.append(False)
                continue
            tf = True
            if diff:
                for n in range(mn+diff,mx-diff+1,diff):

                    #print(i,diff,n,e)
                    if n not in e:
                        tf = False
                        break
            
            res.append(tf)

        return res
                    