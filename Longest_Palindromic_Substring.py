class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_sub_str = ""

        i = 0
        while(i < len(s)):
            
            j = i
            while(j < len(s)):

                sub_str = s[i : j + 1]

                if(sub_str == sub_str[-1 : : -1]):
                    if(len(sub_str) > len(max_sub_str)):
                        max_sub_str = sub_str

                j += 1
            i += 1
        
        return max_sub_str

s = "cbbd"
obj = Solution()
result = obj.longestPalindrome(s)
print(result)