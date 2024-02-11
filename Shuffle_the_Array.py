class Solution:
    def shuffle(self, nums: list, n: int) -> list:
        
        ansList = []

        i = 0
        j = n
        while (i < n):
            ansList.append(nums[i])
            ansList.append(nums[j])
            i += 1
            j += 1

        return ansList

nums = [1,1,2,2]
n = 2
obj = Solution()
solution = obj.shuffle(nums, n)
print(solution)