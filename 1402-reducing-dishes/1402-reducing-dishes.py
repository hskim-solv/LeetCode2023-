class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        res=[]
        for i in range(1,len(satisfaction)+1):
            box = 0
            for i, e in enumerate(satisfaction[-i:], 1):
                box += i*e
            res.append(box)
        return max(0,max(res))