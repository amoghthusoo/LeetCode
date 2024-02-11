class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list, target: int) -> int:
        
        count = 0
        for element in hours:
            if element >= target:
                count += 1

        return count


hours = [5,1,4,2,2]
target = 6
obj = Solution()
solution = obj.numberOfEmployeesWhoMetTarget(hours, target)
print(solution)