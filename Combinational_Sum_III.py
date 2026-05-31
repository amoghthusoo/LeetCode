class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        
        def generate(arr, i, k, n, stack, total, result):

            if(total == n and len(stack) == k):
                result.append(stack.copy())
                return

            if(i == 9 or total > n or len(stack) > k):
                return
            
            stack.append(arr[i])
            generate(arr, i + 1, k, n, stack, total + arr[i], result)
            stack.pop()
            generate(arr, i + 1, k, n, stack, total, result)


        arr = [i for i in range(1, 10)]
        result = []
        generate(arr, 0, k, n, [], 0, result)

        return result

k = 4
n = 1
obj = Solution()
result = obj.combinationSum3(k, n)
print(result)        