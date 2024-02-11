class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        
        count = 0

        for string in words:
            
            if(s.find(string) == 0):
                count += 1

        return count


words = ["a","a"]
s = "aa"
obj = Solution()
solution = obj.countPrefixes(words, s)
print(solution)