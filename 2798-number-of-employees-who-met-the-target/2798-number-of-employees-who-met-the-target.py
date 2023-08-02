class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(cnt if h >= target else 0 for h,cnt in Counter(hours).items())