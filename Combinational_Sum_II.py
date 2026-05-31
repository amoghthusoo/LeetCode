class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
        def generate(arr, index, total, stack, result):

            if(total == 0):
                result.append(stack.copy())
            
            if(total < 0):
                return 
            
            if(index >= len(arr)):
                return
            
            for i in range(index, len(arr)):

                if(i > index and arr[i] == arr[i - 1]):
                    continue
                    
                stack.append(arr[i])
                _sum = total - arr[i]
                generate(arr, i + 1, _sum, stack, result)
                stack.pop()

        
        candidates.sort()
        result = []
        generate(candidates, 0, target, [], result)
        return result
    

arr = [10,1,2,7,6,1,5]
target = 8
obj = Solution()
result = obj.combinationSum2(arr, target)
print(result)