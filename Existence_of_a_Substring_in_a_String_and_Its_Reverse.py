class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        
        rev_s = s[-1::-1]
        
        i = 0
        while(i < len(s) - 1):

            if(s[i] + s[i + 1] in rev_s):
                return True

            i += 1

        return False

s = "leetcode"
obj = Solution()
out = obj.isSubstringPresent(s)
print(out)
