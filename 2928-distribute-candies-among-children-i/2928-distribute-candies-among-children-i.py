class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        '''
        count = 0
        for i in range(min(n, limit)+1):
            for j in range(min(n-i, limit)+1):
                k = n-i-j
                if 0 <= k <= limit:
                    count += 1
        return count
        '''
        
        ans = (n+2)*(n+1)//2

        if (n:= n - limit-1) < 0: return ans
        ans-= 3*(n+2)*(n+1)//2

        if (n:= n - limit-1) < 0: return ans
        ans+= 3*(n+2)*(n+1)//2

        if (n:= n - limit-1) < 0: return ans
        ans-= (n+2)*(n+1)//2

        return ans