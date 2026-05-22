class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        index_dict = dict()

        max_len = -1

        for i, ch in enumerate(s):
            
            if(ch not in index_dict):
                index_dict[ch] = i
            
            else:
                temp_len = i - index_dict[ch] - 1
                if(temp_len > max_len):
                    max_len = temp_len
        
        return max_len

s = "cbzxy"
obj = Solution()
result = obj.maxLengthBetweenEqualCharacters(s)
print(result)