class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:

        """        
        n = len(batteryPercentages)
        ans = 0 
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i]:
                for j in range(1,n-i):
                    if batteryPercentages[i+j]:
                        batteryPercentages[i+j] -= 1
                ans += 1
        return ans
        """
        cnt = 0
        for Percentage in batteryPercentages:
            cnt += Percentage > cnt
        return cnt