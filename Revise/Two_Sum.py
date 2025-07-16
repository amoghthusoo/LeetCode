class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        nums_map = {}

        for i, e in enumerate(nums):
            if(e not in nums_map):
                nums_map[e] = {i}
            else:
                nums_map[e].add(i)
        
        for i, e in enumerate(nums):
            if((target - e) in nums_map):
                indices = nums_map[target - e]
                it = iter(indices)
                for _ in range(len(indices)):
                    index = next(it)
                    if(index != i):
                        return [i, index]

nums = [2,7,11,15] 
target = 9
obj = Solution()
solution = obj.twoSum(nums, target)
print(solution)