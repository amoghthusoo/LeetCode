class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        
        intr_ans = []
        for i in range(rows):
            for j in range(cols):
                intr_ans.append((abs(rCenter - i) + abs(cCenter - j), [i, j]))
        
        intr_ans.sort()
        ans = []
        
        for e in intr_ans:
            ans.append(e[1])
        
        return ans

rows = 1
cols = 2
rCenter = 0
cCenter = 0
obj = Solution()
result = obj.allCellsDistOrder(rows, cols, rCenter, rCenter)
print(result)