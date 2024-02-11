class Solution:
    def countAsterisks(self, s: str) -> int:
        
        count = 0
        pairMem = False

        for ch in s:

            if (not pairMem and ch == "*"):
                count += 1
            elif (ch == "|"):
                pairMem = not pairMem

        return count


s = "yo|uar|e**|b|e***au|tifu|l"
obj = Solution()
solution = obj.countAsterisks(s)
print(solution)