class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        i = 0

        prefix = ""
        while(True):

            try:
                cur_ch = strs[0][i]
            except:
                return prefix
    
            for e in strs:

                try:
                    if(e[i] != cur_ch):
                        return prefix
                except:
                    return prefix
            
            prefix += cur_ch
            
            i += 1


strs = ["ab", "a"]
obj = Solution()
result = obj.longestCommonPrefix(strs)
print(result)