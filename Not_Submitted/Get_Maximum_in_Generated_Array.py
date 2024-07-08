class Solution:
    
    def getMaximumGenerated(self, n: int) -> int:

        if(n == 0):
            return 0
        
        arr = [0, 1]

        i = 2
        while(i <= n):


            if(i % 2 == 0):
                arr.append(arr[i // 2])
            else:

                arr.append(arr[(i - 1) // 2] + arr[((i - 1) // 2) + 1])

            i += 1

        return max(arr)

n = 7
obj = Solution()
out = obj.getMaximumGenerated(n)
print(out)