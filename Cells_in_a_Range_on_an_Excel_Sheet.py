class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        c1, r1, c2, r2 = s[0], int(s[1]), s[3], int(s[4])

        outList = []

        for column in range(ord(c1), ord(c2) + 1):

            for row in range(r1, r2 + 1):

                outList.append(chr(column) + str(row))
        
        return outList
                
s = "A1:F1"
obj = Solution()
solution = obj.cellsInRange(s)
print(solution)