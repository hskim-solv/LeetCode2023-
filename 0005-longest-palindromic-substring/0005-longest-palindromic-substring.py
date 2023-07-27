class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        for i in range(len(s)-1):
            j = len(s)

            while len(res) < j-i:
                j -= 1
                if s[i] == s[j]:
                    mid, mod = divmod(j-i, 2)
                    if mod:
                        p1, p2 = i+mid, i+mid+1
                    else:
                        p1,p2 = i+mid-1,i+mid+1
                    while s[p1] == s[p2]:
                        #print(i,p1,p2,j)
                        if p1 <= i:
                            res = s[i:j+1]
                            break
                        p1 -= 1
                        p2 += 1


                
        return res