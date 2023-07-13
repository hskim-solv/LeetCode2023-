class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        l = [i**2 for i in range(1,int(n**(1/2))+1)]
        res = 1
        if n in l:
            return res
        ll = l
        lll= []
        while res < n:
            res += 1
            for i in l:
                ni = n-i
                for j in ll:
                    if ni == j:
                        return res
                    elif ni > j:
                        lll.append(i+j)
            ll = lll
            lll =[]
        return res
