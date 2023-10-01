class Solution:
    def digitCount(self, num: str) -> bool:
        
        i = 0
        while (i < len(num)):

            if (num.count(str(i)) != int(num[i])):
                return False

            i += 1

        return True

num = "030"
obj = Solution()
solution = obj.digitCount(num)
print(solution)