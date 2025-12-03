from collections import deque

class Solution:
    def check(self, nums: list[int]) -> bool:
        
        def is_sorted(arr):

            i = 0
            while(i < len(arr) - 1):

                if(nums[i] > nums[i + 1]):
                    return False

                i += 1
            
            return True

        nums = deque(nums)

        for _ in range(len(nums)):

            if(is_sorted(nums)):
                return True
            
            nums.append(nums.popleft())
        
        return False

nums = [3,4,5,1,2]
obj = Solution()
result = obj.check(nums)
print(result)