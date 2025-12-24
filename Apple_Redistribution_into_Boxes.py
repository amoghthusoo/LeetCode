class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        
        total = sum(apple)
        capacity.sort(reverse = True)

        for i, c in enumerate(capacity):
            total -= c 

            if(total <= 0):
                return i + 1

apple = [1,3,2]
capacity = [4,3,1,5,2]
obj = Solution()
result = obj.minimumBoxes(apple, capacity)
print(result)            