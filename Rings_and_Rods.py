class Solution:
    def countPoints(self, rings: str) -> int:
        
        interList = ["" for i in range(10)]

        i = 1
        while (i < len(rings)):

            interList[int(rings[i])] += rings[i - 1]

            i += 2

        count = 0
        for rod in interList:

            if ('R' in rod and 'G' in rod and 'B' in rod):
                count += 1

        return count

rings = "G4"
obj = Solution()
solution = obj.countPoints(rings)
print(solution)