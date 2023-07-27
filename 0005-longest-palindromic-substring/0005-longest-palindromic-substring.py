class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        length = len(s)-1
        for i in range(length):
            j = length
            while len(res) <= j-i:
                
                if s[i] == s[j]:
                    if j-i < 3:
                        res = s[i:j+1]
                        break
                    p3, p4 = i, j

                    mid, mod = divmod(j-i, 2)
                    mid += i
                    if mod:
                        p1, p2 = mid, mid+1
                    else:
                        p1, p2 = mid-1, mid+1

                    while not(s[p1] != s[p2] or s[p3] != s[p4]):
                        if p3 >= p1:
                            res = s[i:j+1]
                            break
                        p1 -= 1
                        p2 += 1
                        p3 += 1
                        p4 -= 1
                j -= 1


                
        return res