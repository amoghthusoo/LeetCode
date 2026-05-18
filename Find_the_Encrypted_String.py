class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        
        ans = ""
        for i, ch in enumerate(s):
            ans += s[(i + k) % len(s)]
        return ans

s = "aaa"
k = 1
obj = Solution()
result = obj.getEncryptedString(s, k)
print(result)
