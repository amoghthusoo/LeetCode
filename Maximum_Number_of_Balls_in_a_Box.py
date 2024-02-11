class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        def sum_of_digits(num):

            total = 0
            for digit in str(num):
                total += int(digit)

            return total
        
        interDict = {}

        for i in range(lowLimit, highLimit + 1):

            box_num = sum_of_digits(i)

            if box_num not in interDict:
                interDict[box_num] = 1
            else:
                interDict[box_num] += 1

        return max(interDict.values())


lowLimit = 19
highLimit = 28
obj = Solution()
solution = obj.countBalls(lowLimit, highLimit)
print(solution)