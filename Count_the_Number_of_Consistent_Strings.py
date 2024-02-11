class Solution:
    def countConsistentStrings(self, allowed: str, words: list) -> int:
        
        count = 0

        for word in words:

            for letter in word:

                if letter not in allowed:
                    break
            else:
                count += 1

        return count


allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
obj = Solution()
solution = obj.countConsistentStrings(allowed, words)
print(solution)