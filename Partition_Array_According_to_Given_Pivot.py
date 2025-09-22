class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        
        left = []
        right = []
        count = 0

        for num in nums:

            if(num < pivot):
                left.append(num)
            elif(num > pivot):
                right.append(num)
            else:
                count += 1

        return left + [pivot for _ in range(count)] + right
    
nums = [9,12,5,10,14,3,10]
pivot = 10
obj = Solution()
out = obj.pivotArray(nums, pivot)
print(out)
