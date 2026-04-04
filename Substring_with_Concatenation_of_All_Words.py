from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:

        ans = []
        occr_dict = Counter(words)
        window_size = len(words) * len(words[0])

        if(len(s) < window_size):
            return []

        i = 0
        while(i < len(s) - window_size + 1):

            window = s[i : i + window_size]

            check_mem = True
            temp_occr_dict = {}
            for j in range(0, len(window), len(words[0])):

                target_word = window[j : j + len(words[0])]

                if(target_word in occr_dict):

                    if(target_word not in temp_occr_dict):
                        temp_occr_dict[target_word] = 1
                    else:
                        temp_occr_dict[target_word] += 1
                
                else:
                    check_mem = False
                    break
            
            
            if(check_mem and temp_occr_dict == occr_dict):
                ans.append(i)

            i += 1
        
        return ans

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
obj = Solution()
result = obj.findSubstring(s, words)
print(result)