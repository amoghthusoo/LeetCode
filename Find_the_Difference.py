class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        tList = []

        for ch in t:
            tList.append(ch)
        
        for ch in s:

            if ch in tList:
                del(tList[tList.index(ch)])
            
        return tList[0]

        
        
s = "a"
t = "aa"
obj = Solution()
solution = obj.findTheDifference(s, t)
print(solution)