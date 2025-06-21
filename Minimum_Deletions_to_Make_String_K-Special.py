from collections import Counter
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        
        occr_dict = dict(Counter(word))
        freqs = sorted(occr_dict.values())
        ans = int(2 ** 31 - 1)
        for i in range(len(freqs)):
            
            delete_count = 0
            j = 0
            while(j < i):
                delete_count += freqs[j]
                j += 1

            j = i + 1
            while(j < len(freqs)):

                if(freqs[j] > freqs[i] + k):
                    delete_count += freqs[j] - freqs[i] - k
                j += 1

            if(delete_count < ans):
                ans = delete_count
        
        return ans

word = "aabcaba"
k = 0
obj = Solution()
result = obj.minimumDeletions(word, k)
print(result)
            