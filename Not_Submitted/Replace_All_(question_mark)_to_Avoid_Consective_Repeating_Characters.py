from random import randint

class Solution:
    def modifyString(self, s: str) -> str:

        out_str = ""

        i = 0
        while(i < len(s)):

            if(s[i] != '?'):
                out_str += s[i]

            else:

                if(i == 0):
                    
                    temp_alpha = list(range(97, 123))
                    
                    if(len(s) >= 2):

                        if(s[i + 1] == '?'):
                            pass
                        else:
                            temp_alpha.remove(ord(s[1]))

                    out_str += chr(temp_alpha[randint(0, len(temp_alpha) - 1)])


                elif (i == len(s) - 1):
                    temp_alpha = list(range(97, 123))
                    temp_alpha.remove(ord(out_str[i - 1]))
                    out_str += chr(temp_alpha[randint(0, len(temp_alpha) - 1)])


                else:

                    temp_alpha = list(range(97, 123))
                    
                    if(s[i + 1] == '?'):
                        temp_alpha.remove(ord(out_str[i - 1]))
                        out_str += chr(temp_alpha[randint(0, len(temp_alpha) - 1)])

                    else:
                        temp_alpha.remove(ord(out_str[i - 1]))
                        
                        try:
                            temp_alpha.remove(ord(s[i + 1]))
                        except:
                            pass
                        
                    
                        out_str += chr(temp_alpha[randint(0, len(temp_alpha) - 1)])
            
            i += 1

        return out_str        
    
s = "a?a"
obj = Solution()
out = obj.modifyString(s)
print(out)