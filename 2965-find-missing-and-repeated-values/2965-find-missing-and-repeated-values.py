class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = set(range(1,len(grid)**2+1))
        count_dict = Counter(chain(*grid))
        return [count_dict.most_common(1)[0][0],*(res-set(count_dict.keys()))]
