class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        
        interList = [0]

        for element in gain:
            interList.append(interList[-1] + element)

        return max(interList)


gain = [-4,-3,-2,-1,4,3,2]
obj = Solution()
solution = obj.largestAltitude(gain)
print(solution)