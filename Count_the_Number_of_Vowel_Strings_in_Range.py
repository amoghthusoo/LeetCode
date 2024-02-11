class Solution:
    def vowelStrings(self, words: list, left: int, right: int) -> int:

        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']

        for i in range(left, right + 1):

            if (words[i][0] in vowels and words[i][-1] in vowels):
                count += 1

        return count

words = ["hey","aeo","mu","ooo","artro"]
left = 1
right = 4
obj = Solution()
solution = obj.vowelStrings(words, left, right)
print(solution)