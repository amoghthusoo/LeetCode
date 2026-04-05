class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        ans = 0
        freq_dict = dict()

        i = 0
        j = 0

        early_break = True
        while(j < len(s)):
            
            while(len(freq_dict) != 3 and j < len(s)):

                if(s[j] not in freq_dict):
                    freq_dict[s[j]] = 1
                else:
                    freq_dict[s[j]] += 1

                j += 1

            if(j == len(s) and len(freq_dict) < 3 and early_break):
                break
            else:
                early_break = False

            if(len(freq_dict) == 3):
                ans += len(s) - j + 1

            while(len(freq_dict) == 3):

                if(s[i] in freq_dict):
                    freq_dict[s[i]] -= 1
                    
                    if(freq_dict[s[i]] == 0):
                        freq_dict.pop(s[i])
                
                if(len(freq_dict) == 3):
                    ans += len(s) - j + 1

                i += 1
        
        return ans

s = "acbbcac"
obj = Solution()
result = obj.numberOfSubstrings(s)
print(result)
