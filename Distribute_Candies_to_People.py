class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        
        ans = [0 for _ in range(num_people)]

        inc = 1
        i = 0
        while(candies >= 0):

            if(inc <= candies):
                ans[i] += inc
            else:
                ans[i] += candies
            
            candies -= inc

            inc += 1
            i = (i + 1) % num_people
        
        return ans

candies = 10
num_people = 3
obj = Solution()
result = obj.distributeCandies(candies, num_people)
print(result)