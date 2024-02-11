class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        
        count_of_1s = list()

        for row in mat:
            count_of_1s.append(row.count(1))

        return [count_of_1s.index(max(count_of_1s)), max(count_of_1s)]

mat = [[0,0],[1,1],[0,0]]
obj = Solution()
solution = obj.rowAndMaximumOnes(mat)
print(solution)