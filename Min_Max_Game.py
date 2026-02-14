class Solution:
    def minMaxGame(self, nums: list[int]) -> int:

        if(len(nums) == 1):
            return nums[0]
        
        while(True):
            
            temp = []
            turn = "min"
            i = 0
            while(i < len(nums)):

                if(turn == "min"):
                    temp.append(min(nums[i], nums[i + 1]))
                    turn = "max"
                
                else:
                    temp.append(max(nums[i], nums[i + 1]))
                    turn = "min"
                
                i += 2
            
            if(len(temp) != 1):
                nums = temp
            
            else:
                return temp[0]

nums = [810,831,908,631,554,917,392,544]
obj = Solution()
result = obj.minMaxGame(nums)
print(result)