class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1

        skipped = False
        r1 = True
        while(i < j):

            if(s[i] == s[j]):
                i += 1
                j -= 1
            
            else:
                
                if(skipped):
                    r1 = False
                    break

                skipped = True    
                i += 1

        if(r1):
            return True
        
        i = 0
        j = len(s) - 1

        skipped = False
        r2 = True
        while(i < j):

            if(s[i] == s[j]):
                i += 1
                j -= 1
            
            else:
                
                if(skipped):
                    r2 = False
                    break
                
                skipped = True
                j -= 1

        return r1 or r2

s = "abc"
obj = Solution()
result = obj.validPalindrome(s)
print(result)        