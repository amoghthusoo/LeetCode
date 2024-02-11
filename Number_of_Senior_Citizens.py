class Solution:
    def countSeniors(self, details: list[str]) -> int:
        
        count = 0
        for element in details:

            if (int(element[-4:-2]) > 60):
                count += 1
        
        return count

details = ["1313579440F2036","2921522980M5644"]
obj = Solution()
solution = obj.countSeniors(details)
print(solution)