class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 1
        intervals.sort()
        #print(intervals)
        while i < len(intervals):
            if intervals[i-1][1] >= intervals[i][0]:
                if intervals[i-1][1] < intervals[i][1]:
                    intervals[i-1][1] = intervals[i][1]
                del intervals[i]
            else:
                i += 1
        return intervals