class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        
        ans = 0

        i = 0
        while(i < len(s)):
            j = i
            while(j < len(s)):

                substring = s[i : j + 1]

                if(substring.count("0") <= k or substring.count("1") <= k):
                    ans += 1

                j += 1
            i += 1

        return ans
    
s = "10101"
k = 1
obj = Solution()
result = obj.countKConstraintSubstrings(s, k)
print(result)