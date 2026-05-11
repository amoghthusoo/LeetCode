class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:

        even = []
        odd = []

        i = 0
        while(i < len(nums)):
            try:
                even.append(nums[i])
            except:
                pass
                
            try:
                odd.append(nums[i + 1])
            except:
                pass
             
            i += 2

        even.sort()
        odd.sort()
        odd.reverse()

        out = []
        while(len(out) != len(nums)):

            try:
                out.append(even.pop(0))
            except:
                pass
            
            try:
                out.append(odd.pop(0))
            except:
                pass

        return out
    
nums = [4,1,2,3]
obj = Solution()
out = obj.sortEvenOdd(nums)
print(out)