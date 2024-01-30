class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        n = len(batteryPercentages)
        ans = 0 
        for i,device in enumerate(batteryPercentages):
            if device:
                for j in range(1,n-i):
                    if batteryPercentages[i+j]:
                        batteryPercentages[i+j] -= 1
                ans += 1
            #print(i,ans,batteryPercentages)
        return ans