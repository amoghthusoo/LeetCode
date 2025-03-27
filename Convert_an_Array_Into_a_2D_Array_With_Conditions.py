class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        
        out = [[]]

        for num in nums:

            i = 0
            while(i < len(out)):

                if(num not in out[i]):
                    out[i].append(num)
                    break

                i += 1
            
            else:
                out.append([num])

        return out

nums = [1,2,3,4]
obj = Solution()
out = obj.findMatrix(nums)
print(out)