class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        counter = 0

        while (num != 0):

            if (num % 2 == 0):
                num /= 2
            else:
                num -= 1

            counter += 1

        return counter

num = 123
obj = Solution()
solution = obj.numberOfSteps(num)
print(solution)