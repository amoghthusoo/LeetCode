from copy import deepcopy
class Solution:

    def simulate(self, arr, curr, dir):
        
        while(curr >= 0 and curr < len(arr)):

            if(arr[curr] == 0):

                if(dir == "r"):
                    curr += 1
                else:
                    curr -= 1
            
            elif(arr[curr] > 0):
                arr[curr] -= 1

                if(dir == "r"):
                    dir = "l"
                else:
                    dir = "r"

                if(dir == "r"):
                    curr += 1
                else:
                    curr -= 1

    def countValidSelections(self, nums: list[int]) -> int:
        
        zero_indices = []
        for i, e in enumerate(nums):
            if(e == 0):
                zero_indices.append(i)

        ans = 0

        for i in zero_indices:
            arr = deepcopy(nums)
            self.simulate(arr, i, "l")
            if(sum(arr) == 0):
                ans += 1
            
            arr = deepcopy(nums)
            self.simulate(arr, i, "r")
            if(sum(arr) == 0):
                ans += 1
        
        return ans

             
nums = [1,0,2,0,3]
obj = Solution()
result = obj.countValidSelections(nums)
print(result)
