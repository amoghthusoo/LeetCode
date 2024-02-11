class Solution:
    def isHappy(self, n: int) -> bool:
        
        nStr : str = str(n)
        trackList = []
        
        while (True):

            digitsSquaredNum = 0
            for element in nStr:
                digitsSquaredNum += int(element) ** 2

            nStr = str(digitsSquaredNum)

            if (int(nStr) == 1):
                return True
            elif (int(nStr) in trackList):
                return False
            
            trackList.append(digitsSquaredNum)
            


n = 2
obj = Solution()
solution = obj.isHappy(n)
print(solution)