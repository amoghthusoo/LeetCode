class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        index_map = dict()

        for idx, ch in enumerate(word):
            if(ch not in index_map):
                index_map[ch] = [idx]
            else:
                index_map[ch].append(idx)
        
        ans = 0
        for ch, idx in index_map.items():
            if(ch.islower() and ch.upper() in index_map and max(index_map[ch]) < min(index_map[ch.upper()])):
                ans += 1
        
        return ans


word = "aaAbcBC"
obj = Solution()
result = obj.numberOfSpecialChars(word)
print(result)