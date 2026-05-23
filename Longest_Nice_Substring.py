class Solution:
    def is_nice(self, sub_str):
        
        sub_str = set(sub_str)

        it = iter(sub_str)
        for e in it:
            
            if(e.islower()):
                if(e.upper() not in sub_str):
                    return False
            
            else:
                if(e.lower() not in sub_str):
                    return False
                
        return True

    def longestNiceSubstring(self, s: str) -> str:
        
        max_nice_str = ""
        i = 0
        while(i < len(s)):

            j = i
            while(j < len(s)):

                sub_str = s[i : j + 1]

                if(self.is_nice(sub_str) and (len(sub_str) > len(max_nice_str))):
                    max_nice_str = sub_str

                j += 1
            i += 1

        return max_nice_str

s = "c"
obj = Solution()
result = obj.longestNiceSubstring(s)
print(result)