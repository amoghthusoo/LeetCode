class Solution:
    def has_8_chars(self, s):
        
        if(len(s) >= 8):
            return True
        
        return False
    
    def has_lowercase(self, s : str):

        for e in s:
            if(e.islower()):
                return True
        
        return False
    
    def has_uppercase(self, s : str):

        for e in s:
            if(e.isupper()):
                return True
        
        return False
    
    def has_digit(self, s : str):

        for e in s:
            if(e.isdigit()):
                return True

        return False

    def has_special_char(self, s : str):

        chars = set(list("!@#$%^&*()-+"))

        for e in s:
            if(e in chars):
                return True
        
        return False
    
    def no_adjacent(self, s : str):

        i = 1
        while(i < len(s)):
            
            if(s[i] == s[i - 1]):
                return False
            
            i += 1
        
        return True

    def strongPasswordCheckerII(self, password: str) -> bool:
        
        if(self.has_8_chars(password) and self.has_digit(password) and self.has_lowercase(password) and self.has_special_char(password) and self.has_uppercase(password) and self.no_adjacent(password)):
            return True

        return False


password = "IloveLe3tcode!"
obj = Solution()
result = obj.strongPasswordCheckerII(password)
print(result)
