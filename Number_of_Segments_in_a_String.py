class Solution:
    def countSegments(self, s: str) -> int:
        
        return len(s.split())


s = "Hello"
obj = Solution()
solution = obj.countSegments(s)
print(solution)
