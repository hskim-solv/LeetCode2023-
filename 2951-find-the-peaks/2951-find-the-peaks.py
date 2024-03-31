class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        '''
        length = len(mountain)
        res = []
        for i in range(1, length-1):
            if mountain[i-1] < mountain[i]:
                if mountain[i] > mountain[i+1]:
                    res.append(i)
        return res
        '''
        return [i for i in range(1, len(mountain)-1) if mountain[i-1] < mountain[i] and mountain[i] > mountain[i+1]]
