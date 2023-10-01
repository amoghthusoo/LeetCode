class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        checkStr : str = ""
        for character in s:

            if (character.isupper()):
                character = character.lower()

            if (character.isalnum()):
                checkStr += character
        
        revStr : str = ""

        i = len(checkStr) - 1
        while (i >= 0):
            revStr += checkStr[i]
            i -= 1

        if (checkStr == revStr):
            return True
        else:
            return False

x = ""
obj = Solution()
solution = obj.isPalindrome(x)
print(solution)