class Solution:
    def countTestedDevices(self, batteryPercentages: list[int]) -> int:
        
        tested = 0

        i = 0
        while(i < len(batteryPercentages)):

            if(batteryPercentages[i] > 0):
                tested += 1
                
                j = i + 1
                while(j < len(batteryPercentages)):

                    batteryPercentages[j] -= 1

                    j += 1

            i += 1

        return tested