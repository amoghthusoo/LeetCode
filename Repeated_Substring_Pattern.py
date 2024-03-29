class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        for i in range(len(s)//2):

            if(len(s) % (i + 1) == 0):

                substring = s[0 : i + 1]

                lowerBound = 0
                upperBound = i + 1
                while(True):
                    
                    
                    if(substring != s[lowerBound : upperBound]):
                        break
                    else:

                        if(upperBound == len(s)):
                            return True
                    
                        lowerBound += len(substring)
                        upperBound += len(substring)

        return False


s = "abac"
obj = Solution()
out = obj.repeatedSubstringPattern(s)
print(out)