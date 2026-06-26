class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        
        ans = float("inf")
        i = 0
        while(i < len(nums)):

            j = i + 1
            while(j < len(nums)):

                k = j + 1
                while(k < len(nums)):

                    if(nums[i] < nums[j] and nums[j] > nums[k]):
                        ans = min(ans, nums[i] + nums[j] + nums[k])

                    k += 1
                j += 1
            i += 1
        
        return ans if ans != float("inf") else -1