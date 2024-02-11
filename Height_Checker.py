class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        
        count = 0

        expected = [i for i in heights]
        expected.sort()

        i = 0
        while (i < len(heights)):

            if (heights[i] != expected[i]):
                count += 1
            
            i += 1

        return count

heights = [1,2,3,4,5]
obj = Solution()
solution = obj.heightChecker(heights)
print(solution)
