class Solution:
    def myAtoi(self, s: str) -> int:
        
        if(len(s) == 0):
            return 0
        
        s = s.lstrip()
        
        try:
            s = s.split()[0]
        except:
            return 0


        interStr = ""
        i = 0
        while (i < len(s)):

            if (i == 0 and s[0] in ["+", "-"]):
                interStr += s[0]

            elif (s[i].isdigit()):
                interStr += s[i]

            else:
                break

            i += 1


        if(len(interStr) != 0):
            try:
                s = int(interStr)    
            except:
                return 0
        else:
            return 0
        
        if(s < int(-(2 ** 31))):
            s = int(-(2 ** 31))
        elif(s > int(2 ** 31 - 1)):
            s = int (2 ** 31 - 1)

        return s


s = " "
obj = Solution()
out = obj.myAtoi(s)
print(out)
