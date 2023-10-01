class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        def reverseNum(n : int) -> int:

            n = str(n)
            outStr = ""

            i = len(n) - 1
            while (i >= 0):

                outStr += n[i]
                i -= 1

            return int(outStr)
        
        firstReverse = reverseNum(num)
        secondReverse = reverseNum(firstReverse)

        if (secondReverse == num):
            return True
        else:
            return False


num = 1800
obj = Solution()
solution = obj.isSameAfterReversals(num)
print(solution)