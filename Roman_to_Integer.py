class Solution:
    def romanToInt(self, s: str) -> int:

        romanDict : dict =  {
                                "I" : 1,
                                "V" : 5,
                                "X" : 10,
                                "L" : 50,
                                "C" : 100,
                                "D" : 500,
                                "M" : 1000
                            }
        
        numList = []

        i = 0
        while (i < len(s)):

            if (i == len(s) - 1):
                numList.append(romanDict[s[i]])
            elif ((s[i] == "I") and (s[i + 1] not in ["V", "X"])):
                numList.append(romanDict[s[i]])
            elif ((s[i] == "I") and (s[i + 1] in ["V", "X"])): 
                numList.append(-romanDict[s[i]])
            elif ((s[i] == "X") and (s[i + 1] not in ["L", "C"])): 
                numList.append(romanDict[s[i]])
            elif ((s[i] == "X") and (s[i + 1] in ["L", "C"])): 
                numList.append(-romanDict[s[i]])
            elif ((s[i] == "C") and (s[i + 1] not in ["D", "M"])): 
                numList.append(romanDict[s[i]])
            elif ((s[i] == "C") and (s[i + 1] in ["D", "M"])): 
                numList.append(-romanDict[s[i]])
            else:
                numList.append(romanDict[s[i]])

            i += 1
        
        return sum(numList)
            
s = "MCMXCIV"
obj = Solution()
solution = obj.romanToInt(s)
print(solution)