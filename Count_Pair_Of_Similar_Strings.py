class Solution:
    def similarPairs(self, words: list[str]) -> int:
        count = 0

        i = 0
        while(i < len(words) - 1):

            j = i + 1
            while(j < len(words)):

                if(set(words[i]) == set(words[j])):
                    count += 1

                j += 1
            i += 1
        
        return count
    
words = ["aabb","ab","ba"]
obj = Solution()
out = obj.similarPairs(words)
print(out)