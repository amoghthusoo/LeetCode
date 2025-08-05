class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:

        taken = set()

        i = 0
        while(i < len(fruits)):
            
            j = 0
            while(j < len(baskets)):

                if(fruits[i] <= baskets[j] and j not in taken):
                    taken.add(j)
                    break

                j += 1
            i += 1

        return len(baskets) - len(taken)

fruits = [3,6,1]
baskets = [6,4,7]

obj = Solution()
result = obj.numOfUnplacedFruits(fruits, baskets)
print(result)
