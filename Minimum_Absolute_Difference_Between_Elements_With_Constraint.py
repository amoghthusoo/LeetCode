from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: list[int], x: int) -> int:
        
        min_diff = int(2 ** 31 - 1)

        i = j = 0
        sl = SortedList()
        while(i < len(nums)):
            
            # j = 0
            while(j <= i - x):
                
                sl.add(nums[j])
                j += 1

            if(len(sl) != 0):
                index = sl.bisect(nums[i])

                if(index == 0):
                    diff = abs(nums[i] - sl[index])
                elif(index == len(sl)):
                    diff = abs(nums[i] - sl[-1])
                else:
                    diff = min(abs(nums[i] - sl[index]), abs(nums[i] - sl[index - 1]))
                
                if(diff < min_diff):
                    min_diff = diff

            i += 1

        return min_diff

nums = [4,3,2,4]
x = 2
obj = Solution()
result = obj.minAbsoluteDifference(nums, x)
print(result)
