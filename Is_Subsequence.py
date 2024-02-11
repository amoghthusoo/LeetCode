class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        tList = []

        for ch in t:
            tList.append(ch)

        i = 0
        while (i < len(s)):

            try:
                if (tList[i] != s[i]):
                    del(tList[i])
                    i -= 1
                
                i += 1
            except:
                return False
        
        return True

s = "axc"
t = "ahbgdc"
obj = Solution()
solution = obj.isSubsequence(s, t)
print(solution)