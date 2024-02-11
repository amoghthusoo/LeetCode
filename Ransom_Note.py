class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransomNote = list(ransomNote)
        magazine = list(magazine)

        try:
            for letter in ransomNote:
                magazine.pop(magazine.index(letter))
        except:
            return False

        return True
    
ransomNote = "aa"
magazine = "aab"
obj = Solution()
solution = obj.canConstruct(ransomNote, magazine)
print(solution)