class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        curr_sum = sum(nums[0:k])
        max_avg = curr_sum/k
        
        i = 0
        j = k

        while(j < len(nums)):

            curr_sum -= nums[i]
            curr_sum += nums[j]

            curr_avg = curr_sum / k

            if(curr_avg > max_avg):
                max_avg = curr_avg

            i += 1
            j += 1
        
        return max_avg

nums = [5]
k = 1
obj = Solution()
result = obj.findMaxAverage(nums, k)
print(result)
