from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        
        i = 0
        j = k
        window = SortedList(nums[0 : k])
        ans = []

        while(j < len(nums)):


            if(k % 2 == 0):
                ans.append((window[k // 2] + window[k // 2 - 1])/2)
            else:
                ans.append(window[k//2])

            window.remove(nums[i])
            window.add(nums[j])
            i += 1
            j += 1

        if(k % 2 == 0):
            ans.append((window[k // 2] + window[k // 2 - 1])/2)
        else:
            ans.append(window[k//2])
            
        return ans
    
nums = [1,4,2,3]
k = 4
obj = Solution()
result = obj.medianSlidingWindow(nums, k)
print(result)    