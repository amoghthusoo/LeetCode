class Solution:
    def firstPalindrome(self, words: list) -> str:
        
        def isPalindrome(word : str) -> bool:

            checkStr = ""
            
            i = len(word) - 1
            while (i >= 0):
                checkStr += word[i]
                i -= 1

            if (word == checkStr):
                return True
            else:
                return False
            

        for element in words:
            if (isPalindrome(element)):
                return element 
        else:
            return "" 


words = ["def","ghi"]
obj = Solution()
solution = obj.firstPalindrome(words)
print(solution)