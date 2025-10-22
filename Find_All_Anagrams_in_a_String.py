from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        if(len(p) > len(s)):
            return []

        target_dict = Counter(p)
        freq_dict = dict()

        for i in range(len(p)):

            if(s[i] not in freq_dict):
                freq_dict[s[i]] = 1
            else:
                freq_dict[s[i]] += 1

        i = 0   
        j = len(p) - 1
        ans = []
        if(freq_dict == target_dict):
            ans.append(i)

        while(i < len(s) - len(p)):
            
            freq_dict[s[i]] -= 1
            if(freq_dict[s[i]] == 0):
                freq_dict.pop(s[i])
            i += 1

            j += 1
            if(s[j] not in freq_dict):
                freq_dict[s[j]] = 1
            else:
                freq_dict[s[j]] += 1
            

            if(freq_dict == target_dict):
                ans.append(i)

        return ans


s = "abab"
p = "ab"
obj = Solution()
result = obj.findAnagrams(s, p)
print(result)
