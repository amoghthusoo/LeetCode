class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        wordList = s.split()
        return len(wordList[-1])

s = s = "luffy is still joyboy"
obj = Solution()
solution = obj.lengthOfLastWord(s)
print(solution)