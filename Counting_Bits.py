class Solution:
    def countBits(self, n: int) -> list:
        
        ansList = []

        for i in range(n + 1):
            ansList.append(str(bin(i))[2:].count('1'))

        return ansList


n = 5
obj = Solution()
solution = obj.countBits(n)
print(solution)