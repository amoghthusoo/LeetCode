from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> list:
    
        allComb = list(combinations(list(range(1, n + 1)), k))
        combList = []

        for i in allComb:
            combList.append(list(i))

        return combList

n = 4
k = 2
obj = Solution()
solution = obj.combine(n, k)
print(solution)

    