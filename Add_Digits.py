class Solution:
    def addDigits(self, num: int) -> int:

        num = str(num)

        def adder(num):

            total = 0
            for digit in num:
                total += int(digit)

            return str(total)
        
        result = None
        
        while True:

            result = adder(num)
            num = result

            if (len(result) == 1):
                break

        return int(result)


num = 0
obj = Solution()
solution = obj.addDigits(num)
print(solution)