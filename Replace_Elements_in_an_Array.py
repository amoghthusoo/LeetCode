class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        
        map = dict()

        for i, num in enumerate(nums):
            map[num] = i 
        
        for op in operations:

            old = op[0]
            new = op[1]

            index = map[old]
            nums[index] = new 
            map.pop(old)
            map[new] = index

        return nums

nums = [1,2,4,6]
operations = [[1,3],[4,7],[6,1]]
obj = Solution()
result = obj.arrayChange(nums, operations)
print(result)