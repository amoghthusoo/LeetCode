class Solution:
    def kidsWithCandies(self, candies: list, extraCandies: int) -> list:
        

        ansList = []

        for element in candies:

            if (element + extraCandies >= max(candies)):
                ansList.append(True)
            else:
                ansList.append(False)

        return ansList
    
candies = [12,1,12]
extraCandies = 10
obj = Solution()
solution = obj.kidsWithCandies(candies, extraCandies)
print(solution)