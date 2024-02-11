class Solution:
    def numOfStrings(self, patterns: list, word: str) -> int:
        
        count = 0

        for element in patterns:

            if (element in word):
                count += 1

        return count

patterns = ["a","a","a"]
word = "ab"
obj = Solution()
solution = obj.numOfStrings(patterns, word)
print(solution)