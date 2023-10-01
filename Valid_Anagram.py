class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def strToList(_str) -> list:
            
            strList = []
            for ch in _str:
                strList.append(ch)
            
            return strList
        
        sList = strToList(s)
        tList = strToList(t)

        for element in tList:

            if (element not in sList):
                return False
            else:
                del(sList[sList.index(element)])

        if (len(sList) == 0):
            return True
        else:
            return False

s = "aacc"
t = "ccac"
obj = Solution()
solution = obj.isAnagram(s, t)
print(solution)