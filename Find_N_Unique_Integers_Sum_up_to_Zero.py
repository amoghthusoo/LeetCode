class Solution:
    def sumZero(self, n: int) -> list[int]:
        
        evenMem = None

        if (n % 2 == 0):
            evenMem = True
        else:
            evenMem = False

        
        outList = list()
        i = - (n // 2)
        while (len(outList) < n):

            if (evenMem and i == 0):
                i += 1
                continue

            outList.append(i)
            i += 1
        
        return outList





n = 1
obj = Solution()
solution = obj.sumZero(n)
print(solution)