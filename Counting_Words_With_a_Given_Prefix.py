class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        
        count = 0

        for word in words:

            try:
                if (word.index(pref) == 0):
                    count += 1
            except:
                pass

        return count

words = ["leetcode","win","loops","success"]
pref = "code"
obj = Solution()
solution = obj.prefixCount(words, pref)
print(solution)