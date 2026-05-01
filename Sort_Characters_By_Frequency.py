from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count_dict = Counter(s)

        char_freq_arr = []

        for ch, freq in count_dict.items():
            char_freq_arr.append([freq, ch])
        
        char_freq_arr.sort(reverse = True)

        ans = ""

        for freq_ch in char_freq_arr:

            for _ in range(freq_ch[0]):
                ans += freq_ch[1]
        
        return ans

s = "tree"
obj = Solution()
result = obj.frequencySort(s)
print(result)