class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        
        prev = groups[0]
        ans = [words[0]]

        i = 1
        while(i < len(groups)):

            if(prev != groups[i]):
                ans.append(words[i])
                prev = groups[i]

            i += 1
        
        return ans

words = ["a","b","c","d"]
groups = [1,0,1,1]
obj = Solution()
result = obj.getLongestSubsequence(words, groups)
print(result)