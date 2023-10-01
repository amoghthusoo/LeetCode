class Solution:
    def intersection(self, nums: list) -> list:
        
        ansList = []

        i = 0
        while (i < len(nums[0])):

            inMemory = True

            j = 0
            while (j < len(nums)):

                if (nums[0][i] not in nums[j]):

                    inMemory = False
                    break

                j += 1

            if (inMemory):
                ansList.append(nums[0][i])

            i += 1 

        ansList.sort()

        return ansList


nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
obj = Solution()
solution = obj.intersection(nums)
print(solution)