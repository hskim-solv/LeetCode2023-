class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        cum = 0
        for i in range(1,len(s)+1):
            
            if not set(s[i:])&set(s[cum:i]):
                res.append(i-cum)
                cum += res[-1]
                
        return res