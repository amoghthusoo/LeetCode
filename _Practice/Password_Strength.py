class Solution:
    def passwordStrength(self, password: str) -> int:
        
        password_set = set(password)

        ans = 0
        for ch in password_set:
            if(ch.islower()):
                ans += 1
            elif(ch.isupper()):
                ans += 2
            elif(ch.isnumeric()):
                ans += 3
            else:
                ans += 5
        
        return ans