from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        max_len = -1

        i = 0
        while(i < len(s)):

            j = i
            while(j < len(s)):

                occr_dict = dict(Counter(s[i : j + 1]))
                freq = list(occr_dict.values())     

                for e in freq:
                    if(e > 2):
                        break
                else:
                    current_len = j - i + 1

                    if(current_len > max_len):
                        max_len = current_len

                j += 1
            i += 1

        return max_len

s = "aaaa"
obj = Solution()
result = obj.maximumLengthSubstring(s)
print(result)