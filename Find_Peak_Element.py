class Solution:
    def findPeakElement(self, nums: list) -> int:
        
        neg_inf = -int(2 ** 31) - 1
        nums.insert(0, neg_inf)
        nums.append(neg_inf)
        
        i = 0
        while(i <= len(nums)):

            if (nums[i] > nums[i - 1] and nums[i] > nums[i + 1]):
                return i - 1
            
            i += 1

nums = [1,2,1,3,5,6,4]
obj = Solution()
solution = obj.findPeakElement(nums)
print(solution)