class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        res = ""
        for i in range(len(s)-1):
            j = len(s)-1

            while len(res) <= j-i:

                if s[i] == s[j]:
                    p1,p2 = i+1,j-1
                    while s[p1] == s[p2]:
                        p1 += 1
                        p2 -= 1
                        if p1 > p2:
                            res = s[i:j+1]
                            break

                j -= 1
                
        if res:
            return res
        return s[0]
        