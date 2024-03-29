class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        
        count = 0

        for string in words1:

            if(words1.count(string) == 1 and words2.count(string) == 1):
                count += 1

        return count


words1 = ["a","ab"]
words2 = ["a","a","a","ab"]
obj = Solution()
out = obj.countWords(words1, words2)
print(out)