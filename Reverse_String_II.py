from math import ceil
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        ans = ""
        groups = ceil(len(s)/k)
        i = 0
        while(i < groups):
            
            start = i * k 
            end = i * k + k

            if(i != groups - 1):
                sub_str = s[start : end]
            else:
                sub_str = s[start : ]

            if(i % 2 == 0):
                ans += sub_str[-1::-1]
            else:
                ans += sub_str

            i += 1
        
        return ans 

s = "abcdefg"
k = 2
obj = Solution()
result = obj.reverseStr(s, k)
print(result)