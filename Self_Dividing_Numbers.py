class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list:
        
        def isSelfDividing(num):

            if ('0' in str(num)):
                return False

            for digit in str(num):

                if (num % int(digit) != 0):
                    return False
                
            return True 

        ansList = []

        for i in range(left, right + 1):

            if (isSelfDividing(i)):
                ansList.append(i)

        return ansList


left = 47
right = 85
obj = Solution()
solution = obj.selfDividingNumbers(left, right)
print(solution)