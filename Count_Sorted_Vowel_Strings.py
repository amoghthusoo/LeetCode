class Solution:
    def countVowelStrings(self, n: int) -> int:
        return int((n + 1) * (n + 2) * (n + 3) * (n + 4) / 24)

n = 1
solution = Solution()
result = solution.countVowelStrings(n)
print(result)