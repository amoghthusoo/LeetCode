class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        possibleSoutions = []

        i = 0
        while(i <= len(num) - 3):
            if(num[i] == num[i + 1] == num[i + 2]):
                possibleSoutions.append(int(num[i] * 3))

            i += 1

        if(len(possibleSoutions) == 0):
            return ""
        else:
            maxElement = max(possibleSoutions)

            if(maxElement == 0):
                return "000"
            else:
                return str(maxElement)

num = "42352338"
obj = Solution()
out = obj.largestGoodInteger(num)
print(out)