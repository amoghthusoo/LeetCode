class Solution:
    def replaceDigits(self, s: str) -> str:
        

        def shift(c : str, x : int):
           return chr(ord(c) + x)  
        
        ansStr : str = ""

        i = 0
        while (i < len(s)):
            if (i % 2 == 0):
                ansStr += s[i]
            else:
                ansStr += shift(s[i-1], int(s[i]))
            i += 1
        
        s = ansStr

        return s

        

s = "a1b2c3d4e"
obj = Solution()
solution = obj.replaceDigits(s)
print(solution)