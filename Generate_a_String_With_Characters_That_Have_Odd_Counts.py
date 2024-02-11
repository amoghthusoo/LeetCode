class Solution:
    def generateTheString(self, n: int) -> str:
        
        if (n == 1):
            return 'a'
        else:
            outStr = ""

            if (n % 2 == 0):
                outStr += 'a'
                for i in range(n - 1):
                    outStr += 'b'
            else:
                outStr += "ab"
                for i in range(n - 2):
                    outStr += 'c'

            return outStr

n = 1
obj = Solution()
solution = obj.generateTheString(n)
print(solution)