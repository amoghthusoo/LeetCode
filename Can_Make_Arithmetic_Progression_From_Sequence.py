class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        
        arr.sort()
        d = arr[1] - arr[0]

        i = 0
        while(i < len(arr) - 1):
            if(arr[i + 1] - arr[i] != d):
                return False
            
            i += 1
        return True


arr = [1,2,4]
obj = Solution()
out = obj.canMakeArithmeticProgression(arr)
print(out)