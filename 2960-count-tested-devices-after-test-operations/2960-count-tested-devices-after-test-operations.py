class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
      
        ans = 0 
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i]:
                for j in range(i,len(batteryPercentages)):
                    if batteryPercentages[j]:
                        batteryPercentages[j] -= 1
                ans += 1
        return ans
        """
        cnt = 0
        for Percentage in batteryPercentages:
            cnt += Percentage > cnt
        return cnt
        """