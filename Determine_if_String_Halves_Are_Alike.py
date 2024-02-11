class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        a = s[0 : len(s) // 2]
        b = s[len(s) // 2 :]

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        vowel_count_a = 0
        vowel_count_b = 0

        for vowel in vowels:

            vowel_count_a += a.count(vowel)
            vowel_count_b += b.count(vowel)

        if (vowel_count_a == vowel_count_b):
            return True
        else:
            return False
    


s = "textbook"
obj = Solution()
solution = obj.halvesAreAlike(s)
print(solution)