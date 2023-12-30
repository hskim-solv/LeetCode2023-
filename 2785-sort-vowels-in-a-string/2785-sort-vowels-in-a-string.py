class Solution:
    def sortVowels(self, s: str) -> str:
        
        vowels = "aeiouAEIOU"
        q = []
        for ch in sorted(s):
            if ch in vowels:
                q.append(ch)
        s = list(s)
        q = q[::-1]
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = q.pop()
        return "".join(s)
