class Solution:
    def findComplement(self, num: int) -> int:
        
        binary = str(bin(num))[2:]
        
        compliment = ""
        for digit in binary:
            if (digit == '1'):
                compliment += '0'
            else:
                compliment += '1'

        i = 0
        j = len(compliment) - 1

        decimal = 0

        while (i < len(compliment)):
            
            decimal += int(compliment[j]) * 2 ** i

            i += 1
            j -=1

        return decimal

num = 1
obj = Solution()
solution = obj.findComplement(num)
print(solution)