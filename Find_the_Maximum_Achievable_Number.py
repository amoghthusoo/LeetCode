class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        
        return num + t * 2

num = 3
t = 2
obj = Solution()
solution = obj.theMaximumAchievableX(num, t)
print(solution)