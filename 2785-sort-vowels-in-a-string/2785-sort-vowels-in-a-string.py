class Solution:
    def sortVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = "aeiouAEIOU"
        q = []
        for ch in sorted(s):
            if ch in vowels:
                q.append(ch)
        q = q[::-1]
        for i in range(len(s)):
            if s[i] in vowels:
                s_list[i] = q.pop()
        return "".join(s_list)
