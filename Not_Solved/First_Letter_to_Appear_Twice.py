# NOT SOLVED
class Solution:
    def repeatedCharacter(self, s: str) -> str:

        i = 0
        while (i < len(s)):

            j = i + 1
            while (j < len(s)):

                if (s[i] == s[j]):
                    return s[i]

                j += 1

            i += 1
            

s = "abcdd"
obj = Solution()
solution = obj.repeatedCharacter(s)
print(solution)

