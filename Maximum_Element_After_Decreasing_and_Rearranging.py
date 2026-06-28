class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        
        arr.sort()
        arr[0] = 1
        
        i = 1
        while(i < len(arr)):
            
            trial = arr[i - 1] + 1
            if(trial < arr[i]):
                arr[i] = trial
            i += 1
        
        return arr[-1]

arr = [100,1,1000]
obj = Solution()
result = obj.maximumElementAfterDecrementingAndRearranging(arr)
print(result)