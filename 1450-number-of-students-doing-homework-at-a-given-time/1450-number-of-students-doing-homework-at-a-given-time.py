class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum( s <= queryTime and e >= queryTime for s, e in zip(startTime, endTime) )