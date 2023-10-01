class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        def binStrToInt(binStr : str) -> int:

            decNum = 0
            i = 0
            while (i < len(binStr)):
                
                binNum += int(binStr[i]) * 2 ** (len(binStr) - 1 - i)
                i += 1

            return decNum
        

        decNum1 = binStrToInt(a)
        decNum2 = binStrToInt(b)

        outBin = str(bin(decNum1 + decNum2)[2:])

        return outBin

a = "1010"
b = "1011"
obj = Solution()
solution = obj.addBinary(a, b)
print(solution)