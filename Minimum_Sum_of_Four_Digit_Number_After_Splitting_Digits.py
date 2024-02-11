class Solution:
    def minimumSum(self, num: int) -> int:
        
        numList = []
        while(num != 0):
            numList.append(num % 10)
            num //= 10

        numList.sort()

        return (numList[0] * 10 + numList[3]) + (numList[1] * 10 +  numList[2])

num = 4009
obj = Solution()
solution = obj.minimumSum(num)
print(solution)