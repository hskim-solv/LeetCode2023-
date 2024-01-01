class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = list(range(1,len(grid)**2+1))
        count_dict = Counter(chain(*grid))
        for k,v in count_dict.items():
            if v == 1:
                res.remove(k)
        if res[0] != count_dict.most_common(1)[0][0]:
            res.reverse()
        return res
