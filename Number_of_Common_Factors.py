class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        minNum = min(a,b)
        maxNum = max(a, b)

        count = 0
        for i in range(1, minNum + 1):

            if (minNum % i == 0 and maxNum % i == 0):
                count += 1

        return count

a = 25
b = 30
obj = Solution()
solution = obj.commonFactors(a, b)
print(solution)