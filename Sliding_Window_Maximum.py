from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        
        window = SortedList(nums[0 : k])
        ans = [window[-1]]

        i = 0
        j = k
        while(j < len(nums)):

            window.remove(nums[i])
            window.add(nums[j])

            ans.append(window[-1])

            i += 1
            j += 1
        
        return ans
    
nums = [1]
k = 1
obj = Solution()
result = obj.maxSlidingWindow(nums, k)
print(result)