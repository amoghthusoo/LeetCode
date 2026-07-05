class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ans = 0
        i = 0
        while(i < len(s)):
            temp = ""
            j = i
            while(j < len(s)):

                temp += s[j]

                if(temp == temp[::-1]):
                    ans += 1

                j += 1
            i += 1
        
        return ans