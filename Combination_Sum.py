class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        def generate(arr, stack, i, total, target, result):
    
            if(total > target or i == len(arr)):
                return
            
            if(total == target):
                result.append(stack.copy())
                return
            
            stack.append(arr[i])
            total += arr[i]
            generate(arr, stack, i, total, target, result)

            stack.pop()
            total -= arr[i]
            generate(arr, stack, i + 1, total, target, result)

        result = []
        generate(candidates, [], 0, 0, target, result)
        return result