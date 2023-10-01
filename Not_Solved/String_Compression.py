#NOT SOLVED
from collections import Counter
class Solution:
    def compress(self, chars: list) -> int:
        
        occDict = dict(Counter(chars))
        s = ""

        for key in occDict:

            if (occDict[key] == 1):
                s += key
            
            elif (occDict[key] > 1):
                s += key

                for num in str(occDict[key]):
                    s += num

        chars = list(s)

        return len(chars), chars


chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
obj = Solution()
solution, chars = obj.compress(chars)
print(solution, chars)