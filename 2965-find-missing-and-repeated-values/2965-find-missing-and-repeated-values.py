class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count_dict = Counter(chain(*grid))
        return [count_dict.most_common(1)[0][0],*(set(range(1,len(grid)**2+1))-set(count_dict.keys()))]
