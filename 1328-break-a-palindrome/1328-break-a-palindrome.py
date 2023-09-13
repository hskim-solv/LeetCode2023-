class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        palindrome = list(palindrome)
        for i in range(len(palindrome)):
            if palindrome[i] != "a":
                tmp = palindrome[i]
                palindrome[i] = "a"
                if palindrome == palindrome[::-1]:
                    palindrome[i] = tmp
                    continue
                break
        if palindrome == palindrome[::-1]:
            palindrome[-1] = chr(ord(palindrome[-1])+1)
        return "".join(palindrome)
        