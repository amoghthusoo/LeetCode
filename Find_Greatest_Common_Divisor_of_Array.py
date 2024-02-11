class Solution:
    def findGCD(self, nums: list) -> int:
        
        nums.sort()
        lowNum = nums[0]
        highNum = nums[-1]

        i = lowNum
        while True:

            if (lowNum % i == 0 and highNum % i == 0):
                return i
            
            i -= 1

nums = [3,3]
obj = Solution()
solution = obj.findGCD(nums)
print(solution)