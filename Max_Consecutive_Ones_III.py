class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:

            if(k > 0):
                ans = 0
                i = 0
                j = 0
                cnt = 0
                while(j < len(nums)):
                    
                    if(nums[j] == 1):
                        j += 1
                    
                    elif(nums[j] == 0):
                        
                        if(cnt < k):
                            j += 1
                        else:
                            while(cnt >= k and i < j):
                                if(nums[i] == 0):
                                    cnt -= 1
                                i += 1
                            j += 1

                        if(k > 0):    
                            cnt += 1
                    
                    ans = max(ans, j - i)
                
                return ans 

            else:
                ans = 0
                cnt = 0
                i = 0
                while(i < len(nums)):
                    
                    if(nums[i] == 1):
                        cnt += 1
                    else:
                        ans = max(ans, cnt)
                        cnt = 0

                    i += 1
                
                ans = max(ans, cnt)
                
                return ans
    
nums = [1,1,1,0,0,0,1,1,1,1]
k = 0
obj = Solution()
result = obj.longestOnes(nums, k)
print(result)