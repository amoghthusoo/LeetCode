class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        
        result = []
        stack = []
        i = 1
        j = 0
        while(i <= n):
            if(i == target[j]):
                result.append("Push")
                stack.append(i)
                j += 1
            else:
                result.extend(["Push", "Pop"])
            
            if(stack == target):
                return result

            i += 1
        
target = [1,2]
n = 4
solution = Solution()
result = solution.buildArray(target, n)
print(result)