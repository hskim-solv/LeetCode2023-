class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        for i in range(1,len(s)+1):

            if not set(s[i:])&set(s[:i]):
                res.append(i-sum(res))
                
        return res