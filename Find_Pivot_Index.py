class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        
        left_sum = []
        cumm_sum = 0

        i = 0
        while(i < len(nums)):
            left_sum.append(cumm_sum)
            cumm_sum += nums[i]
            i += 1
        
        cumm_sum = 0
        right_sum = []
        i = len(nums) - 1
        while(i >= 0):
            right_sum.append(cumm_sum)
            cumm_sum += nums[i]
            i -= 1
        
        right_sum.reverse()

        i = 0
        while(i < len(left_sum)):

            if(left_sum[i] == right_sum[i]):
                return i

            i += 1

        return -1
    

nums = [1,7,3,6,5,6]
obj = Solution()
result = obj.pivotIndex(nums)
print(result)

