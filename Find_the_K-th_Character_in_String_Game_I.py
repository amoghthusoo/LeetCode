class Solution:
    def kthCharacter(self, k: int) -> str:
        
        s = "a"

        while(len(s) < k):
            temp = ""
            for ch in s:
                temp += chr(((ord(ch) - 97 + 1) % 26) + 97)
            
            s += temp

        return s[k - 1]

k = 5
obj = Solution()
result = obj.kthCharacter(k)
print(result)