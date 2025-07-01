class Solution:
    def possibleStringCount(self, word: str) -> int:
        
        ans = 0
        curr_char = word[0]
        group_size = 1
        i = 1
        while(i < len(word)):

            if(word[i] == curr_char):
                group_size += 1
            else:
                ans += group_size - 1
                group_size = 1
                curr_char = word[i]

            i += 1
        
        ans += group_size - 1

        return ans + 1
    
word = "aaaa"
obj = Solution()
result = obj.possibleStringCount(word)
print(result)