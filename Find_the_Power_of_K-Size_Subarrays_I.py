from collections import deque
class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        
        def is_consecutive(arr):

            for i in range(1, len(arr)):
                if(arr[i] != arr[i - 1] + 1):
                    return False
            
            return True

        ans = []

        window = deque(nums[0 : k])
        j = k - 1

        while(True):

            if(is_consecutive(window)):
                ans.append(window[-1])
            else:
                ans.append(-1)
            
            j += 1

            if(j == len(nums)):
                break

            window.popleft()
            window.append(nums[j])
        
        return ans

nums = [1,3,4]
k = 2
obj = Solution()
result = obj.resultsArray(nums, k)
print(result)
