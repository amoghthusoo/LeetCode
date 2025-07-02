class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        open_count = 0
        close_count = 0

        str1 = ""

        for e in s:
            if(e == "("):
                open_count += 1
                str1 += e

            elif(e == ")"):
                close_count += 1
                if(open_count >= close_count):
                    str1 += e
                else:
                    close_count -= 1

            else:
                str1 += e
        

        open_count = 0
        close_count = 0

        str2 = ""

        i = len(str1) - 1
        while(i >= 0):
            
            if(str1[i] == "("):
                open_count += 1

                if(close_count >= open_count):
                    str2 += str1[i]
                else:
                    open_count -= 1

            elif(str1[i] == ")"):
                close_count += 1
                str2 += str1[i]

            else:
                str2 += str1[i]
            i -= 1
        
        return str2[-1 : :-1]
    
s = "))(("
obj = Solution()
result = obj.minRemoveToMakeValid(s)
print(result)