class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x = str(x)
        revStr = ""

        i = len(x) - 1
        
        while (i >= 0):
            revStr += x[i] 
            i -=1
        
        if (revStr == x):
            return True
        else:
            return False

    
input = 10
obj = Solution()
solution = obj.isPalindrome(input)
print(solution)