class Solution:
    def numSquares(self, n: int) -> int:
        l = [i**2 for i in range(1,int(n**(1/2))+1)]
        res = 1
        if n in l:
            return res
        ll = l
        while res < n:
            lll= set()
            res += 1
            for i in ll:
                ni = n-i
                for j in l:
                    if ni < j:
                        break
                    elif ni == j:
                        return res
                    elif ni > j:
                        lll.add(i+j)
            #print(l,ll,lll)
            ll = lll
        return res
