class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        length = len(pattern)
        s = s.split(" ")
        if length != len(s):
            return False
        dict_matching_str = defaultdict(str)
        for i in range(length):
            if pattern[i] in dict_matching_str:
                if dict_matching_str[pattern[i]] != s[i]:
                    return False
            else:
                dict_matching_str[pattern[i]] = s[i]
        if len(dict_matching_str.keys()) == len(set(dict_matching_str.values())):
            return True