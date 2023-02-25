class Solution:
    def sortSentence(self, s: str) -> str:
        return re.sub("\d+",""," ".join(sorted(s.split(sep = " "), key = lambda v: v[-1])))
        