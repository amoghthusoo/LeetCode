class Solution:

    def sliceString(self, s: str, k: int) -> str:
        
        sliced = []

        i = 0
        x = 0
        temp = ""
        while (i < len(s)):

            if (x < k):
                temp += s[i]
                x += 1
                i += 1
            else:
                sliced.append(temp)
                temp = ""
                x = 0

        sliced.append(temp)
        
        return sliced
    
    def calculateDigitSum(self, s : str) -> int:
        
        s = list(s)
        s = [int(i) for i in s]

        return sum(s)

    def concatSliced(self, sliced : list[str]) -> str:

        outStr = ""

        for numString in sliced:
            outStr += str(self.calculateDigitSum(numString))

        return outStr

    def digitSum(self, s: str, k: int) -> str:
        
        while(len(s) > k):
            
            sliced = self.sliceString(s, k)
            s = self.concatSliced(sliced)
            
        return s


s = "00000000"
k = 3
obj = Solution()
out = obj.digitSum(s, k)
print(out)
