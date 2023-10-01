class Solution:
    def reverse(self, x: int) -> int:

        x : str = str(x)
        reversedNum : str= ""

        if (int(x) >= 0):

            i = len(x) - 1
            while (i >= 0):
                reversedNum += x[i]
                i -= 1
        
        else:

            reversedNum += '-'
            i = len(x) - 1
            while (i > 0):
                reversedNum += x[i]
                i -= 1

        if (int(reversedNum) > (2 ** 31) - 1) or (int(reversedNum) < (2 ** 31) * (-1)) :
            return 0
        else:
            return int(reversedNum)


input = 1534236469
obj = Solution()
solution = obj.reverse(input)
print(solution)