class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        
        ans = float("inf")
        for i in range(len(landStartTime)):
                
            for j in range(len(waterStartTime)):

                temp = 0
                temp += landStartTime[i] + landDuration[i]

                if(waterStartTime[j] > temp):
                    temp += (waterStartTime[j] - temp)
                
                temp += waterDuration[j]
            
                ans = min(ans, temp)
        

        for i in range(len(waterStartTime)):

            for j in range(len(landStartTime)):

                temp = 0
                temp += waterStartTime[i] + waterDuration[i]

                if(landStartTime[j] > temp):
                    temp += (landStartTime[j] - temp)
                
                temp += landDuration[j]
            
                ans = min(ans, temp)
        
        return ans

landStartTime = [94,85]
landDuration = [20,54]
waterStartTime = [20,4]
waterDuration = [2,35]

obj = Solution()
result = obj.earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration)
print(result)