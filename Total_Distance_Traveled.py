class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:

        dist = 0
        cnt = 0
        while(mainTank > 0):

            mainTank -= 1
            cnt += 1
            dist += 10

            if(cnt == 5):
                cnt = 0
                if(additionalTank > 0):
                    additionalTank -= 1
                    mainTank += 1

        return dist

mainTank = 1
additionalTank = 2
obj = Solution()
result = obj.distanceTraveled(mainTank, additionalTank)
print(result)