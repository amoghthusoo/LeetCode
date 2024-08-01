class Solution:
    def findKOr(self, nums: list[int], k: int) -> int:
        
        bin_arr = [0 for _ in range(31)]

        i = 0
        while(i < len(nums)):

            num = nums[i]
            j = 30
            
            while(num != 0):
                
                bin_arr[j] += num % 2
                num //= 2

                j -= 1

            i += 1

        out_num = 0
        i = 30
        while(i >= 0):

            if(bin_arr[i] >= k):
                out_num += int(2 ** (30 - i))            
            
            i -= 1

        return out_num

nums = [10,8,5,9,11,6,8]
k = 1
obj = Solution()
out = obj.findKOr(nums, k)
print(out)