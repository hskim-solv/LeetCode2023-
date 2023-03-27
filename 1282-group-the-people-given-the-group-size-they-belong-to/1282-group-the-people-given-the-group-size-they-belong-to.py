class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        for i, s in enumerate(groupSizes):
            if s in d:
                d[s].append(i)
            else:
                d[s] = [i]
        return [  v[k*i:k*(i+1)] for k, v in d.items() for i in range(len(v) // k) ]

        
                