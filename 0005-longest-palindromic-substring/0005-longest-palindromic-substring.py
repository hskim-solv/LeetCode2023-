class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        res = ""
        for i in range(len(s)):
            j = len(s)-1

            while i < j:
                if len(res) > j-i:
                    break
                if s[i]==s[j]:
                    p1,p2 = i+1,j-1
                    while s[p1]==s[p2] and p1 <= p2:
                        p1+=1
                        p2-=1
                    if p1 > p2:
                        if len(res) < len(s[i:j+1]):
                            res = s[i:j+1]

                j -= 1
                
        if res:
            return res
        return s[0]
        