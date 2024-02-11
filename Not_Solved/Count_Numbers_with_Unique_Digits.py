# NOT SOLVED BUT ACCEPTED
from collections import Counter

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        def isUnique(num):

            num = str(num)
            occDict = dict(Counter(num))

            for element in occDict.values():
                
                if(element != 1):
                    return False
                
            return True

        count = 0

        for i in range(10 ** n):
            if (isUnique(i)):
                count += 1

        
        
        return count


n = 0
obj = Solution()
solution = obj.countNumbersWithUniqueDigits(n)
print(solution)

"""
0 : 1
1 : 10
2 : 91
3 : 739
4 : 5275
5 : 32491
6 : 168571
7 : 712891
8 : 2345851
"""