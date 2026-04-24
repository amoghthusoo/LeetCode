class Solution:
    def minSwaps(self, s: str) -> int:
        
        s = list(s)
        swaps = 0
        open_count = close_count = 0
        j = -1
        i = 0
        while(i < len(s)):
            
            if(s[i] == "["):
                open_count += 1
            else:
                close_count += 1


            if(close_count > open_count):
                while(s[j] != "["):
                    j -= 1
                s[i], s[j] = s[j], s[i]
                open_count += 1
                close_count -= 1
                swaps += 1

            i += 1

        return swaps

s = "][]["
obj = Solution()
result = obj.minSwaps(s)
print(result)