class Solution:
    def reverseString(self, s: list) -> None:

        s.reverse()
        
        return s

s = ["H","a","n","n","a","h"]
obj = Solution()
solution = obj.reverseString(s)
print(solution)