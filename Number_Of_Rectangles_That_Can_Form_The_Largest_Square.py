from collections import Counter

class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        
        intr_arr = []

        for r in rectangles:
            intr_arr.append(min(r[0], r[1]))


        maxLen = max(intr_arr)

        return intr_arr.count(maxLen)
            

rectangles = [[2,3],[3,7],[4,3],[3,7]]
obj = Solution()
out = obj.countGoodRectangles(rectangles)
print(out)
