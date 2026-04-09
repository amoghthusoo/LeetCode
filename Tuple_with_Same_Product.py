class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        
        map = dict()
        ans = 0

        i = 0
        while(i < len(nums) - 1):

            j = i + 1
            while(j < len(nums)):

                prod = nums[i] * nums[j]
                if(prod not in map):
                    map[prod] = 1
                
                else:
                    ans += 8 * map[prod]
                    map[prod] += 1

                j += 1
            i += 1
        
        return ans 

nums = [2,3,4,6,8,12]
obj = Solution()
result = obj.tupleSameProduct(nums)
print(result)