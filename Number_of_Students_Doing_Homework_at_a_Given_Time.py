class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        
        count = 0
        i = 0
        while (i < len(startTime)):

            if (queryTime in range(startTime[i], endTime[i] + 1)):
                count += 1

            i += 1

        return count
        

startTime = [4]
endTime = [4]
queryTime = 4
obj = Solution()
solution = obj.busyStudent(startTime, endTime, queryTime)
print(solution)