class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        s = s.split()

        previous = -1

        for string in s:
            
            if(string.isdigit()):
                if(int(string) <= previous):
                    return False
                
                else:
                    previous = int(string)

        return True

s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
obj = Solution()
out = obj.areNumbersAscending(s)
print(out)