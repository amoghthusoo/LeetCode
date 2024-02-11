class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if (needle not in haystack):
            return -1
        else:
            return haystack.index(needle)



haystack = "leetcode"
needle = "leeto"
obj = Solution()
solution = obj.strStr(haystack, needle)
print(solution)