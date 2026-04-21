from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        
        i = j = 0
        M = m = nums[0]
        ans = -1
        window = SortedList()
        window.add(nums[0])
        while(True):

            if(M - m <= limit):
                curr_len = j - i + 1
                if(curr_len > ans):
                    ans = curr_len
                
            
                j += 1

                if(j == len(nums)):
                    break
                
                window.add(nums[j])
                
                if(nums[j] > M):
                    M = nums[j]
                
                if(nums[j] < m):
                    m = nums[j]
                    
            else:
                
                while(M - m > limit):
                    
                    window.remove(nums[i])
                    i += 1
                    
                    M = window[-1]
                    m = window[0]

        return ans
        
nums = [8,2,4,7]
limit = 4
obj = Solution()
result = obj.longestSubarray(nums, limit)
print(result)