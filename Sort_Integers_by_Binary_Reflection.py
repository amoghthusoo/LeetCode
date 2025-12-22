class Solution:
    def sortByReflection(self, nums: list[int]) -> list[int]:
        
        intr_arr = []

        for num in nums:

            reversed = int(bin(num)[2 : ][-1::-1], 2)
            intr_arr.append((reversed, num))

        intr_arr.sort()

        ans = []
        for reversed, original in intr_arr:
            ans.append(original)
        
        return ans

nums = [3,6,5,8]
obj = Solution()
result = obj.sortByReflection(nums)
print(result)

