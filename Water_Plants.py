class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        
        steps = 1
        current_capacity = capacity
        i = 0
        while(i < len(plants)):

            current_capacity -= plants[i]

            try:               
                if(plants[i + 1] > current_capacity):
                    steps += (i + 1) * 2
                    current_capacity = capacity
                else:
                    pass
            except:
                return steps
            
            steps += 1
            i += 1


plants = [3,2,4,2,1]
capacity = 6
solution = Solution()
result = solution.wateringPlants(plants, capacity)
print(result)