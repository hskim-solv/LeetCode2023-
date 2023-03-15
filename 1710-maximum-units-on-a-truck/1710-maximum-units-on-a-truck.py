class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        for n, u in sorted(boxTypes, key=lambda x: x[1], reverse = True):
            if n < truckSize:
                truckSize -= n
                res += n * u
            else:
                res += truckSize * u
                break
        return res