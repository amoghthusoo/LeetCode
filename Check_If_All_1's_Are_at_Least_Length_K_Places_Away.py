class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        
        last_one = None
        i = 0
        while(i < len(nums) and nums[i] != 1 ):
            i += 1
        
        last_one = i
        i += 1

        while(i < len(nums)):

            if(nums[i] == 1):
                
                if(i - last_one - 1 < k):
                    return False
                
                last_one = i

            i += 1
        
        return True

nums = [0, 0, 0]
k = 2
obj = Solution()
result = obj.kLengthApart(nums, k)
print(result)
