class Solution:
    def finalValueAfterOperations(self, operations: list) -> int:
        
        x = 0

        for element in operations:
            if element in ["++X", "X++"]:
                x += 1
            else:
                x -= 1

        return x

operations = ["X++","++X","--X","X--"]
obj = Solution()
solution = obj.finalValueAfterOperations(operations)
print(solution)