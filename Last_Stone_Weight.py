from sortedcontainers import SortedList
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        stones = SortedList(stones)

        while(len(stones) != 1):
            
            try:
                x = stones.pop()
            except:
                return 0
            
            y = stones.pop()

            if(x != y):
                stones.add(abs(x - y))

        return stones.pop()        

stones = [2,7,4,1,8,1]
obj = Solution()
result = obj.lastStoneWeight(stones)
print(result)