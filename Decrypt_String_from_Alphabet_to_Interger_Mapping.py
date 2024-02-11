class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        
        values = [i for i in range(1, 27)]
        alphabets = [chr(i) for i in range(97, 123)]
        
        encryptDict = dict(zip(values, alphabets))

        interList = []

        i = 0
        while (i < len(s)):

            try:
                
                if (s[i + 2] == '#'):
                    interList.append(int(s[i:i + 2]))
                    i += 3
                else:
                    interList.append(int(s[i]))
                    i += 1
            
            except:
                
                while (i < len(s)):
                    interList.append(int(s[i]))
                    i += 1

        outStr = ""

        for element in interList:
            outStr += encryptDict[element]


        return outStr

s = "10#11#12"
obj = Solution()
solution = obj.freqAlphabets(s)
print(solution)