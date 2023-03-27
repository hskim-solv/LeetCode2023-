class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        ans = []
        for i, s in enumerate(groupSizes):
            if s in d:
                d[s].append(i)
            else:
                d[s] = [i]
        for k, v in d.items():
            for _ in range(len(d[k])//k):
                ans.append(d[k][:k])
                del d[k][:k]
        return ans
                