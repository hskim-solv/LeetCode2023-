class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote, magazine = list(Counter(ransomNote).items()), Counter(magazine)
        while ransomNote:
            n = ransomNote.pop()
            if n[0] not in magazine:
                return False
            else:
                if n[1] > magazine[n[0]]:
                    return False
        return True